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

class MainPage(models.Model):
    title = models.CharField('Заголовок', max_length=100, default='Главная страница')
    text = models.TextField('Текст', default=None)
    image = models.CharField('Ссылка на картинку', max_length=1000, default='static/main/img/developer.png')
    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'

class DemandPage(models.Model):
    title = models.CharField('Заголовок', max_length=100, default='Востребованность')

    text1 = models.TextField('Текст1', default=None)
    text2 = models.TextField('Текст2', default=None)
    text3 = models.TextField('Текст3', default=None)
    text4 = models.TextField('Текст4', default=None)

    image1 = models.CharField('Ссылка на картинку1', max_length=1000, default='static/main/img/developer.png')
    image2 = models.CharField('Ссылка на картинку2', max_length=1000, default='static/main/img/developer.png')
    class Meta:
        verbose_name = 'Страница востребованность'
        verbose_name_plural = 'Страница востребованность'

class GeoPage(models.Model):
    title = models.CharField('Заголовок', max_length=100, default='География')

    text1 = models.TextField('Текст1', default=None)
    text2 = models.TextField('Текст2', default=None)
    text3 = models.TextField('Текст3', default=None)
    text4 = models.TextField('Текст4', default=None)

    image1 = models.CharField('Ссылка на картинку1', max_length=1000, default='static/main/img/developer.png')
    image2 = models.CharField('Ссылка на картинку2', max_length=1000, default='static/main/img/developer.png')
    class Meta:
        verbose_name = 'Страница география'
        verbose_name_plural = 'Страница география'

class SkillsPage(models.Model):
    title = models.CharField('Заголовок', max_length=100, default='Навыки')

    text1 = models.TextField('Текст1', default=None)
    text2 = models.TextField('Текст2', default=None)


    image1 = models.CharField('Ссылка на картинку1', max_length=1000, default='static/main/img/developer.png')

    class Meta:
        verbose_name = 'Страница навыки'
        verbose_name_plural = 'Страница навыки'
