from django.shortcuts import render
from main.models import Experience
from main.models import Skills
from main.models import Education
from main.models import Project
from main.models import Achievement

# Create your views here.
def show_main(request):
    context = {
        "name": "Muhammad Ghaisan Raya",
        "npm": "2506624493",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "A Computer Science student at Universitas Indonesia interested "
            "in software development and education."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Muhammad Ghaisan Raya",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_skills(request):
    context = {
        "name": "Muhammad Ghaisan Raya",
        "skills_list": Skills.objects.all(),
        }
    return render(request, "skills.html", context)

def show_education(request):
    context = {
        "name": "Muhammad Ghaisan Raya",
        "education_list": Education.objects.all(),
        }
    return render(request, "education.html", context)

def show_project(request):
    context = {
        "name": "Muhammad Ghaisan Raya",
        "project_list": Project.objects.all(),
        }
    return render(request, "project.html", context)

def show_achievement(request):
    context = {
        "name": "Muhammad Ghaisan Raya",
        "achievement_list": Achievement.objects.all(),
        }
    return render(request, "achievement.html", context)
