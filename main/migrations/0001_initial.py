# Generated by Django 4.1.4 on 2023-01-09 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableSalaryVacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(default='', max_length=4, verbose_name='Год')),
                ('avgSalary', models.CharField(default='', max_length=100000, verbose_name='Средняя зарплата в IT')),
                ('avgSalaryVac', models.CharField(default='', max_length=100000, verbose_name='Средняя зарплата Backend-разработчика')),
            ],
        ),
    ]
