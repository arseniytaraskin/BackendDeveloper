from django.db import models

# Create your models here.

# модели для таблиц бд
class TableSalaryVacancies (models.Model):
    year = models.CharField('Год', max_length=4, default='')
    avgSalary = models.CharField('Средняя зарплата в IT', max_length=100000, default='')
    avgSalaryVac = models.CharField('Средняя зарплата Backend-разработчика', max_length=100000, default='')

    #магический метод
    def __str__(self):
        return self.year

    class Meta:
        verbose_name = 'Средние зарплаты'
        verbose_name_plural = 'Средние зарплаты'

class TableCountVacancies (models.Model):
    year = models.CharField('Год', max_length=4, default='')
    avgSalary = models.CharField('Количество вакансий в IT', max_length=100000, default='')
    avgSalaryVac = models.CharField('Количество вакансий по профессии Backend-разработчик', max_length=100000, default='')

    #магический метод
    def __str__(self):
        return self.year

    class Meta:
        verbose_name = 'Количество вакансий'
        verbose_name_plural = 'Количество вакансий'

class TableGeoSalary (models.Model):
    city = models.TextField('Город', default='')
    avgSalary = models.CharField('Уровень зарплат в рублях', max_length=100000, default='')

    #магический метод
    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'З/п по городам'
        verbose_name_plural = 'З/п по городам'

class TableGeoVac (models.Model):
    city = models.TextField('Город', default='')
    proc = models.CharField('Доля вакансий в %', max_length=100000, default='')

    #магический метод
    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Доля вакансий по городам'
        verbose_name_plural = 'Доля вакансий городам'

class TableSkills(models.Model):
    year = models.CharField('Год',max_length=10000, default='')
    skills = models.TextField('Топ 10 навыков', default='')

    #магический метод
    def __str__(self):
        return self.year

    class Meta:
        verbose_name = 'Навыки'
        verbose_name_plural = 'Навыки'