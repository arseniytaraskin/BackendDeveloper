from django.shortcuts import render
from django.http import HttpResponse

from .utils import add_vac
# Create your views here.

from .models import TableSalaryVacancies, TableCountVacancies, TableGeoSalary, TableGeoVac, TableSkills, Vacancy, MainPage, DemandPage, GeoPage, SkillsPage
def about(request):
    mainpage = MainPage.objects.all()[0]
    return render(request, "main/about.html", context={'mainpage':mainpage, 'title':'Главная страница'})

def demand(request):
    table1 = TableSalaryVacancies.objects.all().order_by('year')
    table2 = TableCountVacancies.objects.all().order_by('year')
    demandpage = DemandPage.objects.all()[0]
    return render(request, "main/demand.html", {'table1':table1, 'table2':table2, 'demandpage':demandpage})

def geography(request):
    table1 = TableGeoSalary.objects.all().order_by('-avgSalary')
    table2 = TableGeoVac.objects.all().order_by('-proc')
    geopage = GeoPage.objects.all()[0]
    return render(request, "main/geography.html", {'table1':table1, 'table2':table2, 'geopage':geopage})

def skills(request):
    table = TableSkills.objects.all().order_by('year')
    skillspage = SkillsPage.objects.all()[0]
    return render(request, "main/skills.html", {'table':table, 'skillspage':skillspage})

def vacancies(request):
    add_vac()
    return render(request, "main/vacancies.html", context={'vacancies': Vacancy.objects.order_by('-published_at')[:10]})