from django.shortcuts import render


def home(request):
    return render(request, "core/pages/home.html")


def contact_us(request):
    return render(request, "core/pages/contact_us.html")
