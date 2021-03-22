from django.urls import path

from .views import EmployeeListCreateView, RetrieveUpdateDestroyAPI

urlpatterns = [
    path('', EmployeeListCreateView.as_view(), name='employee_list_create'),
    path('/<int:pk>', RetrieveUpdateDestroyAPI.as_view())
]