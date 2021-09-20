from django.db import models
from django_mysql.models import ListCharField

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=50, unique=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    jobs_posted = models.IntegerField()
    successful_jobs = models.IntegerField()

    def __str__(self):
        return self.name


class Freelancer(models.Model):

    profpic = models.ImageField(
        upload_to="profpics/", default="profpics/avatar.jpg")
    name = models.CharField(max_length=50, unique=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    total_jobs = models.IntegerField()
    total_hrs_worked = models.IntegerField()
    title = models.CharField(max_length=50)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=2000)
    email = models.EmailField(("email address"), unique=True)
    education = models.CharField(max_length=1000, default="engineering")
    languages = ListCharField(
        base_field=models.CharField(max_length=50), size=10, max_length=(10 * 51),
        default=" "
    )
    skills = ListCharField(
        base_field=models.CharField(max_length=50), size=10, max_length=(10 * 51),
        default=" "
    )

    def __str__(self):
        return self.name


class Work(models.Model):
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    freelancer = models.ForeignKey("Freelancer", on_delete=models.CASCADE)
    title = models.CharField(max_length=1000, default="")
    comment = models.CharField(max_length=1000)
    rating = models.IntegerField(default=0)
    time = models.IntegerField(default=0)

    def __str__(self):
        return self.client.name + " -> " + self.freelancer.name


class Project(models.Model):
    freelancer = models.ForeignKey("Freelancer", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    photo = models.ImageField(upload_to="projects/")

    def __str__(self):
        return self.freelancer.name + " - "+self.title


class Certification(models.Model):
    freelancer = models.ForeignKey("Freelancer", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="certificates/")
    issued_by = models.CharField(max_length=100)

    def __str__(self):
        return self.freelancer.name + " - "+self.issued_by
