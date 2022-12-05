from django.shortcuts import render
from django.views.generic import CreateView
from .forms import AddPostModelForm

class AddPostView(CreateView):
    form_class = AddPostModelForm
    template_name = 'add_post_module/add_post_page.html'
    success_url = '/artists'
