from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, "core/home.html")


def historia(request):

    return render(request, "core/about.html")

def services(request):

    return render(request, "core/servicios.html")

def store(request):

    return render(request, "core/visitanos.html")
