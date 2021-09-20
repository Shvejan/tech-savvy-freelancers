from django.contrib import admin
from .models import Freelancer, Work, Project, Client, Certification
# Register your models here.
admin.site.register(Freelancer)
admin.site.register(Work)
admin.site.register(Project)
admin.site.register(Client)
admin.site.register(Certification)
