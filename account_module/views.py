from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views import View
from django.contrib.auth import login, logout
from account_module.forms import RegisterForm, ForgotPasswordForm, ResetPasswordForm
from .models import User
from django.utils.crypto import get_random_string
from django.http import Http404
from .forms import LoginForm
from utils.email_service import send_email

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register_page.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'The email entered is duplicate')
            else:
                new_user = User(email=user_email, email_active_code=get_random_string(72), is_active=False,
                                username=user_email)
                new_user.set_password(user_password)
                new_user.save()
                # todo : send email active code
                send_email('فعال سازی حساب کاربری', new_user.email,{'user':new_user},'emails/active_account.html')
                return redirect(reverse('login_page'))

        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register_page.html', context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login_page.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'your account is not active')
                else:
                    is_password_correct = user.check_password(user_password)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('list_of_persons'))
                    else:
                        login_form.add_error('email', 'No user found')
            else:
                login_form.add_error('email', 'No user found')

        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login_page.html', context)


class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                # todo : show success message to user
                return redirect(reverse('login_page'))
            else:
                # todo : show your account was activated message to user
                pass

        raise Http404


class ForgetPasswordView(View):
    def get(self, request):
        forgot_password_form = ForgotPasswordForm()
        return render(request, 'account_module/forgot_password.html', context={
            'forgot_password_form': forgot_password_form
        })

    def post(self, request):
        forgot_password_form = ForgotPasswordForm(request.POST)
        if forgot_password_form.is_valid():
            user_email = forgot_password_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                # todo send reset password email to user
                send_email('بازیابی کلمه عبور', user.email, {'user': user}, 'emails/forgot_pass.html')
                return redirect(reverse('login_page'))

        return render(request, 'account_module/forgot_password.html', context={
            'forgot_password_form': forgot_password_form
        })


class ResetPasswordView(View):
    def get(self, request, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('login_page'))
        reset_pass_form = ResetPasswordForm()
        return render(request, 'account_module/reset_password.html', context={
            'reset_pass_form': reset_pass_form,
            'user': user
        })

    def post(self,request,active_code):
        reset_pass_form = ResetPasswordForm(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if reset_pass_form.is_valid():
            if user is None:
                return redirect(reverse('login_page'))
            user_new_pass = reset_pass_form.cleaned_data.get('password')
            user.set_password(user_new_pass)
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('login_page'))

        return render(request, 'account_module/reset_password.html', context={
            'reset_pass_form': reset_pass_form,
            'user': user
        })


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect(reverse('login_page'))