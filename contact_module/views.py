from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from django.views.generic.edit import FormView, CreateView
from .forms import ContactUsModelForm
from .models import ContactUs, UserProfile


# Create your views here.

class ContactUsView(CreateView):
    form_class = ContactUsModelForm
    template_name = 'contact_module/contact_us.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ContactUsView, self).get_context_data(**kwargs)
        contact_us = ContactUs.objects.all()
        context['contactus'] = contact_us
        return context


class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile_page.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/contact/create-profile/'


class ProfileListView(ListView):
    model = UserProfile
    template_name = 'contact_module/profile_list_page.html'
    context_object_name = 'profiles'
