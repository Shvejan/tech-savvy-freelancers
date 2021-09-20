from profiles.models import Freelancer
from django.shortcuts import render
from .models import Certification, Freelancer, Project, Work
# Create your views here.


def profilePage(request, profile_name):
    freelancer = Freelancer.objects.get(name=profile_name)
    projects = Project.objects.filter(freelancer=freelancer)
    works = Work.objects.filter(freelancer=freelancer)
    certificates = Certification.objects.filter(freelancer=freelancer)
    return render(request, "profiles/techsavy.html", {"freelancer": freelancer,
                                                      "projects": projects, "works": works,
                                                      "certificates": certificates})
