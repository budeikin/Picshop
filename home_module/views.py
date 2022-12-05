from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from post_module.models import Post
from site_module.models import SiteSetting
from utils.http_service import get_client_ip

# class HomeView(View):
#     def get(self,request):
#         return render(request,'home_module/index.html')


class HomeView(TemplateView):
    template_name = 'home_module/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        context['post'] = posts
        return context


class AboutView(TemplateView):
    template_name = 'home_module/about_page.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        site_setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = site_setting
        return context


def site_header_component(request):
    return render(request, 'shared/site_header.html')


def site_footer_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    return render(request, 'shared/site_footer.html', {
        'site_setting': setting
    })
