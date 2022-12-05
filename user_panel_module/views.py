from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, View
from .forms import EditProfileModelForm, ChangePasswordForm
from account_module.models import User
from django.contrib.auth import logout


# views are here

class UserPanelDashboardView(TemplateView):
    template_name = 'user_panel_module/user_panel_dashboard_page.html'


class EditUserProfilePage(View):
    def get(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(instance=current_user)
        return render(request, 'user_panel_module/edit_profile_page.html', context={
            'form': edit_form,
            'current_user': current_user
        })

    def post(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)
        return render(request, 'user_panel_module/edit_profile_page.html', context={
            'form': edit_form,
            'current_user': current_user
        })


class ChangePasswordPage(View):
    def get(self, request):
        context = {
            'form': ChangePasswordForm()
        }
        return render(request, 'user_panel_module/change_password_page.html', context)

    def post(self, request):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_user: User = User.objects.filter(id=request.user.id).first()
            if current_user.check_password(form.cleaned_data.get('current_password')):
                current_user.set_password(form.cleaned_data.get('password'))
                current_user.save()
                logout(request)
                return redirect(reverse('login_page'))
            else:
                form.add_error('password', 'your password is wrong')

        context = {
            'form': form
        }
        return render(request, 'user_panel_module/change_password_page.html', context)


def user_panel_menu_component(request):
    return render(request, 'user_panel_module/component/user_panel_menu_component.html')
