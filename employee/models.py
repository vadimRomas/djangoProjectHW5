from django.db import models

from company.models import CompanyModel


# Create your models here.
# name surname age profession
class EmployeeModel(models.Model):
    class Meta:
        db_table = 'employee'

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    profession = models.CharField(max_length=255)
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, related_name='employee')
