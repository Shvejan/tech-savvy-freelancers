# Generated by Django 3.1.2 on 2021-09-19 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('jobs_posted', models.IntegerField()),
                ('successful_jobs', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profpic', models.ImageField(default='static/profpics/avatar.jpg', upload_to='static/profpics/')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('total_jobs', models.IntegerField()),
                ('total_hrs_worked', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=2000)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('photo', models.ImageField(default='static/profpics/avatar.jpg', upload_to='static/projects/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.user')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('rating', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.client')),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.user')),
            ],
        ),
    ]
