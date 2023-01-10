from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import TableSalaryVacancies
def about(request):
    return render(request, "main/about.html", {'title':'Главная страница'})

def demand(request):
    table1 = TableSalaryVacancies.objects.all()
    return render(request, "main/demand.html", {'table1':table1})

def geography(request):
    return render(request, "main/geography.html")

def skills(request):
    return render(request, "main/skills.html")