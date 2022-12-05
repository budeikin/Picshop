from django.urls import path
from . import views

urlpatterns =[
    path('',views.ContactUsView.as_view(),name='contact_us_form'),
    path('create-profile/',views.CreateProfileView.as_view(),name='create_profile_page'),
    path('profiles/', views.ProfileListView.as_view(),name='profiles_page')
]