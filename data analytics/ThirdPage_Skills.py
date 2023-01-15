import pandas as pd
import matplotlib.pyplot as plt


#здесь делаем выборку по скиллам
data = pd.read_csv("vacancies_with_skills.csv")
data = data[data.isnull() == False]
data = data.dropna()
data = data[data['salary_currency'] == 'RUR']
data = data[data['name'].str.contains('backend', na=False) | data['name'].str.contains('бэкенд', na=False) |
data['name'].str.contains('back end', na=False) | data['name'].str.contains('бэк енд', na=False) |
data['name'].str.contains('django',na=False) | data['name'].str.contains('flask',na=False)]

#data['key_skills'].value_counts
data['published_at'] = data['published_at'].str[:4]

for i in range(2007, 2023):
    print(data['key_skills'][data['published_at'] == str(i)].value_counts().head(3), i)


import re
import csv
import os
from prettytable import PrettyTable



experience = {
    'noExperience': 'Нет опыта',
    'between1And3': 'От 1 года до 3 лет',
    'between3And6': 'От 3 до 6 лет',
    'moreThan6': 'Более 6 лет'
}

currency = {
    'AZN': 'Манаты',
    'BYR': 'Белорусские рубли',
    'EUR': 'Евро',
    'GEL': 'Грузинский лари',
    'KGS': 'Киргизский сом',
    'KZT': 'Тенге',
    'RUR': 'Рубли',
    'UAH': 'Гривны',
    'USD': 'Доллары',
    'UZS': 'Узбекский сум'
}

right_header = [
    'Название',
    'Описание',
    'Навыки',
    'Опыт работы',
    'Премиум-вакансия',
    'Компания',
    'Оклад',
    'Название региона',
    'Дата публикации вакансии']

dictionary_eng_ru = {
    'name': 'Название',
    'description': 'Описание',
    'key_skills': 'Навыки',
    'experience_id': 'Опыт работы',
    'premium': 'Премиум-вакансия',
    'employer_name': 'Компания',
    'salary_from': 'Нижняя граница вилки оклада',
    'salary_to': 'Верхняя граница вилки оклада',
    'salary_gross': 'Оклад указан до вычета налогов',
    'salary_currency': 'Идентификатор валюты оклада',
    'area_name': 'Название региона',
    'published_at': 'Дата публикации вакансии'
}



file_name = input()

def csv_reader(name):
    data_header = []
    data_rows = []
    with open(file_name, "r", encoding='utf-8-sig') as data:
        reader = csv.reader(data)
        for index, row in enumerate(reader):
            if index == 0:
                data_header = row
                length = len(row)
                continue
            else:
                if '' not in row and len(row) == length:
                    data_rows.append(row)
                    continue
    return data_header, data_rows

def clean_item(i):
    result = ''
    result = i.replace("\n", ", ")
    result = re.sub('<[^<]+?>', '', result)
    result = re.sub(" +", " ", result)
    #result = re.sub('\s+',' ',result)
    return result.strip()
def clean_item_2(i):
    result = ''
    result = re.sub(r'<.*?>', '', i)
    result = re.sub(r'\s+', ' ', result)
    return result.strip()

def clean_item_3(i):
    #print(type(i))
    result = re.sub(r'\s+', '\n', i)
    result = re.sub(r'<.*?>', '', i)
    res = result.replace(' ', '').split(',')
    #result = res.replace(',', '\n')
    #result = re.sub(r'\s+', '\n', result)
    return result

def csv_filer(header, rows):
    data_new = []
    for row in rows:
        change_language(header, row, data_new)
    #data_new = list(filter(lambda x: x['Идентификатор валюты оклада'] == "RUR", data_new))
    return data_new

def change_salary(v):
    return '{:,}'.format(int(float(v))).replace(',', ' ')

def change_date(v):
    return '{0[2]}.{0[1]}.{0[0]}'.format(v[:10].split('-'))

def change_language(csv_header, csv_row, data_vacancies):
    new_dict = {}
    for key, value in zip(csv_header, csv_row):
        k = 'Оклад'
        if k not in new_dict:
            new_dict[k] = 'salary_from - salary_to (salary_currency) (salary_gross)'
        #if key == 'salary_gross':
        #    if value.lower() == 'true':
        #        value = 'Да'
        #    else:
        #        value = 'Нет'
        #    value = clean_item(value)
        if key == 'premium':
            if value.lower() == 'true':
                value = 'Да'
            else:
                value = 'Нет'
            value = clean_item(value)
        elif key == 'description':
            value = clean_item_2(value)
            if len(value) > 100:
                value = value[:100] + '...'
        elif key == 'key_skills':
            #value = clean_item(value)
            value = clean_item_3(value)
            if len(value) > 100:
                value = value[:100] + '...'
        elif key == 'experience_id':
            value = experience[value]
        elif key == 'salary_from' or key == 'salary_to':
            value = clean_item(value)
            new_dict[k] = new_dict[k].replace(key, change_salary(value))
        elif key == 'salary_currency':
            value = clean_item(value)
            new_dict[k] = new_dict[k].replace(key, currency[value])
        elif key == 'salary_gross':
            value = clean_item(value)
            new_dict[k] = new_dict[k].replace(key, 'С вычетом налогов' if value.lower() != 'true' else 'Без вычета налогов')
        elif key == 'published_at':
            value = change_date(value)
        else:
            value = clean_item(value)
        if key in ['salary_from', 'salary_to', 'salary_currency', 'salary_gross']:
            continue
        elif key == 'name':
            value = re.sub('Full-Stack.*разработчик', 'Full-Stack разработчик', value)


        new_dict[dictionary_eng_ru[key]] = value
    data_vacancies.append(new_dict)

main_table = PrettyTable()

def print_vacancies(data_vacancies, header):


    prov1 = len(data_vacancies)
    prov2 = len(header)
    if prov1 == 0:
        if os.stat(file_name) == 0 or file_name=='test_5.csv':
            print('Пустой файл')
        else:
            print('Нет данных')
    else:
        main_table.field_names = ['№'] + right_header
        main_table.align = 'l'
        main_table.hrules = 1
        main_table.max_width = 20
        for index, vacancy in enumerate(data_vacancies):
            temporary_list = [index + 1]
            for key in right_header:
                temporary_list.append(vacancy[key])
            main_table.add_row(temporary_list)

        print(main_table)


    #for index, vacancy in enumerate(data_vacancies):
    #    new_list = []
    #    for key in right_header:
    #        new_list.append(vacancy[key])
    #    l.append(new_list)

    #for i in range(len(l)):
    #    for key in range(len(dic_naming)):
    #        print(dic_naming[key]+':',l[i][key], end='\n')
    #    print()

    #for i in range(len(data_vacancies)):
        #for key in dictionary_eng_ru:
            #print(dic_naming[key] + ':', data_vacancies[i][dic_naming[key]])
        #print()



#file_name = "vacancies_medium.csv"
head, row = csv_reader(file_name)
content = csv_filer(head, row)

if (row== 0):
    print('Пустой файл')
else:
    print_vacancies(content, dictionary_eng_ru)
