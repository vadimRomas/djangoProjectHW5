from django.urls import path

from .views import CompanyListCreateView, RetrieveUpdateDestroyAPI, FilterCity

urlpatterns = [
    path('', CompanyListCreateView.as_view(), name='company_list_create'),
    path('/filter', FilterCity.as_view()),
    path('/<int:pk>', RetrieveUpdateDestroyAPI.as_view())
]
