from rest_framework import status
from rest_framework.generics import ListCreateAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .serializers import CompanySerializers
from .models import CompanyModel


# Create your views here.


class CompanyListCreateView(ListCreateAPIView):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializers


class RetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializers

    def patch(self, *args, **kwargs):
        return super().patch(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)


class FilterCity(ListCreateAPIView):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializers

    def get(self, request, *args, **kwargs):

        qs = CompanyModel.objects.all()
        city = self.request.query_params.get('city')

        if city:
            qs = qs.filter(city__iexact=city)

        res = CompanySerializers(qs, many=True).data
        return Response(res, status.HTTP_200_OK)


