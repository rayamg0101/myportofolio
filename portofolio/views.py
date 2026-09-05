from django.shortcuts import render


def landing_page(request):
    return render(request, "index.html")

def aboutme_page(request):
    return render(request, "Aboutme.html")