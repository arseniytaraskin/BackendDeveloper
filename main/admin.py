from django.contrib import admin

# Register your models here.

from .models import TableSalaryVacancies, TableCountVacancies, TableGeoSalary, TableGeoVac, TableSkills, Vacancy, MainPage, DemandPage, GeoPage, SkillsPage

admin.site.register(TableSalaryVacancies)
admin.site.register(TableCountVacancies)
admin.site.register(TableGeoSalary)
admin.site.register(TableGeoVac)
admin.site.register(TableSkills)
admin.site.register(MainPage)
admin.site.register(DemandPage)
admin.site.register(GeoPage)
admin.site.register(SkillsPage)

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('hh_id', 'name', 'published_at',
                    'key_skills', 'address', 'url',
                    'salary', 'employer',)
