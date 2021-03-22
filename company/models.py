from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


# Create your models here.
class CompanyModel(models.Model):
    class Meta:
        db_table = "company"

    company_name = models.CharField(max_length=50)
    country = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='company')
