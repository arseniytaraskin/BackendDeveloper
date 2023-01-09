from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def about(request):
    return render(request, "main/about.html", {'title':'Главная страница'})

def demand(request):
    return render(request, "main/demand.html")

def geography(request):
    return render(request, "main/geography.html")

def skills(request):
    return render(request, "main/skills.html")