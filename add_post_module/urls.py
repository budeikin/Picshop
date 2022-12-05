from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddPostView.as_view(), name='add_post_page'),
]
