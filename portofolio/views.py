from django.shortcuts import render


def landing_page(request):
    return render(request, "index.html")

def skills_page(request):
    return render(request, "skills.html")