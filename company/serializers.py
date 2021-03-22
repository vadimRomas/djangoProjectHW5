from rest_framework.serializers import ModelSerializer

from .models import CompanyModel


class CompanySerializers(ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = '__all__'

    def create(self, validated_data):
        company = CompanyModel(**validated_data)
        company.save()
        return company
        # company_name
        # country
        # city
        # user
