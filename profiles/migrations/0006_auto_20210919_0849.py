# Generated by Django 3.1.2 on 2021-09-19 08:49

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_freelancer_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancer',
            name='languages',
            field=django_mysql.models.ListCharField(models.CharField(max_length=50), default='English', max_length=510, size=10),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='skills',
            field=django_mysql.models.ListCharField(models.CharField(max_length=50), default=' ', max_length=510, size=10),
        ),
    ]
