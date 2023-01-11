from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import TableSalaryVacancies, TableCountVacancies, TableGeoSalary, TableGeoVac, TableSkills
def about(request):
    return render(request, "main/about.html", {'title':'Главная страница'})

def demand(request):
    table1 = TableSalaryVacancies.objects.all().order_by('year')
    table2 = TableCountVacancies.objects.all().order_by('year')
    return render(request, "main/demand.html", {'table1':table1, 'table2':table2})

def geography(request):
    table1 = TableGeoSalary.objects.all().order_by('-avgSalary')
    table2 = TableGeoVac.objects.all().order_by('-proc')
    return render(request, "main/geography.html", {'table1':table1, 'table2':table2})

def skills(request):
    table = TableSkills.objects.all().order_by('year')
    return render(request, "main/skills.html", {'table':table})