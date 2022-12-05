from django.urls import path
from . import views

urlpatterns = [
    path('', views.PersonListView.as_view(), name='list_of_persons'),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),
    path('pro/<pro>', views.PersonListView.as_view(), name='list_of_professions'),
    path('id/<slug:pk>', views.PersonDetailView.as_view(), name="detail_of_persons"),
]
