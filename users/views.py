from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import UserSerializer
from .models import CustomUser


# Create your views here.


class UserListCreateView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class RetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
