# Generated by Django 4.1.4 on 2023-01-13 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_demandpage_alter_mainpage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='География', max_length=100, verbose_name='Заголовок')),
                ('text1', models.TextField(default=None, verbose_name='Текст1')),
                ('text2', models.TextField(default=None, verbose_name='Текст2')),
                ('text3', models.TextField(default=None, verbose_name='Текст3')),
                ('text4', models.TextField(default=None, verbose_name='Текст4')),
                ('image1', models.CharField(default='static/main/img/developer.png', max_length=1000, verbose_name='Ссылка на картинку1')),
                ('image2', models.CharField(default='static/main/img/developer.png', max_length=1000, verbose_name='Ссылка на картинку2')),
            ],
            options={
                'verbose_name': 'Страница география',
                'verbose_name_plural': 'Страница география',
            },
        ),
    ]
