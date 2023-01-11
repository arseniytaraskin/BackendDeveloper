from django.contrib import admin

# Register your models here.

from .models import TableSalaryVacancies, TableCountVacancies, TableGeoSalary, TableGeoVac, TableSkills

admin.site.register(TableSalaryVacancies)
admin.site.register(TableCountVacancies)
admin.site.register(TableGeoSalary)
admin.site.register(TableGeoVac)
admin.site.register(TableSkills)
