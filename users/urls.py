from django.urls import path

from .views import UserListCreateView, RetrieveUpdateDestroyAPI

urlpatterns = [
    path('', UserListCreateView.as_view(), name='users_list_create'),
    path('/<int:pk>', RetrieveUpdateDestroyAPI.as_view())
]
