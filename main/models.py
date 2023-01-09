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