from django.db import models
import datetime
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


class Vacancy(models.Model):
    hh_id = models.CharField(max_length=100, default='0000')
    name = models.CharField(
        'Название вакансии',
        max_length=100,
        default='name'
    )
    published_at = models.DateTimeField(
        'Дата публикации',
        default=datetime.datetime(2023, 1, 7, 15, 10, 47, 625508)
    )
    description = models.TextField('Описание', blank=True, null=True)
    key_skills = models.TextField('Навыки', blank=True, null=True)
    address = models.TextField('Город', blank=True, null=True)
    url = models.URLField('Ссылка', max_length=100, null=True)
    salary = models.CharField(
        'зарплата',
        max_length=100,
        blank=True,
        null=True
    )
    employer = models.CharField(
        'Имя нанимателя',
        max_length=100,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Вакансии hh.ru'
        verbose_name_plural = 'Вакансии hh.ru'
