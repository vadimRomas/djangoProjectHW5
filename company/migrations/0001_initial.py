# Generated by Django 3.1.7 on 2021-03-17 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=254)),
                ('city', models.CharField(max_length=254)),
            ],
            options={
                'db_table': 'company',
            },
        ),
    ]