# Generated by Django 3.1.2 on 2021-09-19 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20210919_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='photo',
            field=models.ImageField(upload_to='certificates/'),
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='profpic',
            field=models.ImageField(default='profpics/avatar.jpg', upload_to='profpics/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='photo',
            field=models.ImageField(upload_to='projects/'),
        ),
    ]
