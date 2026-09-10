from django.shortcuts import render
from main.models import Experience

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
