import pandas as pd
import matplotlib.pyplot as plt

import csv
import math
import re
import numpy as np

def print_data(date, data_salary_min, data_skills, data_area):
    if len(date) < 10:
        size = len(date)
    else:
        size = 10
    print('Самые высокие зарплаты:')
    for i in range(0, size):
        if date[i]['salary_average'] % 10 == 1:
            rur = 'рубль'
        elif 1 < date[i]['salary_average'] % 10 < 5:
            rur = 'рубля'
        else:
            rur = 'рублей'
        print(
            f"""    {i + 1}) {date[i]['name']} в компании "{date[i]['employer_name']}" - {date[i]['salary_average']} {rur} (г. {date[i]['area_name']})""")

    print('\nСамые низкие зарплаты:')

    for i in range(0, size):
        if data_salary_min[i]['salary_average'] % 10 == 1:
            rur = 'рубль'
        elif 1 < data_salary_min[i]['salary_average'] % 10 < 5:
            rur = 'рубля'
        else:
            rur = 'рублей'
        print(
            f"""    {i + 1}) {data_salary_min[i]['name']} в компании "{data_salary_min[i]['employer_name']}" - {data_salary_min[i]['salary_average']} {rur} (г. {data_salary_min[i]['area_name']})""")

    print(f'\nИз {len(data_skills)} скиллов, самыми популярными являются:')
    for i in range(0, 10 if len(data_skills) > 10 else len(data_skills)):
        if data_skills[i][1] % 10 == 1 or data_skills[i][1] % 10 == 0 or 4 < data_skills[i][1] % 100 < 22 or 4 < \
                data_skills[i][1] % 10 < 9:
            ras = 'раз'
        else:
            ras = 'раза'
        print(
            f"""    {i + 1}) {data_skills[i][0]} - упоминается {data_skills[i][1]} {ras}""")

    print(f'\nИз {len(data_area)} городов, самые высокие средние ЗП:')
    counter = 0
    i = 0
    while counter != 10 and i < len(date):
        if data_area[i][2] >= math.floor(len(date) / 100):
            if 4 < data_area[i][2] < 21 or data_area[i][2] % 10 > 4:
                vac = 'вакансий'
            elif data_area[i][2] % 10 == 1:
                vac = 'вакансия'
            else:
                vac = 'вакансии'
            if data_area[i][1] % 10 == 1:
                rur = 'рубль'
            elif 1 < data_area[i][1] % 10 < 5 and not 9 < data_area[i][1] % 100 < 21:
                rur = 'рубля'
            else:
                rur = 'рублей'
            print(
                f"""    {counter + 1}) {data_area[i][0]} - средняя зарплата {data_area[i][1]} {rur} ({data_area[i][2]} {vac})""")
            counter += 1
        i += 1


def take_area(main_data):
    data = {}
    data_sort = []
    for vacancy in main_data:
        if data.__contains__(vacancy['area_name']):
            data[vacancy['area_name']] = [(int(vacancy['salary_average']) + int(data[vacancy['area_name']][0])),
                                          data[vacancy['area_name']][1] + 1]
        else:
            data[vacancy['area_name']] = [int(vacancy['salary_average']), 1]
    for key in data:
        data_sort.append([key, math.floor(data[key][0] / data[key][1]), data[key][1]])
    data_sort = sorted(data_sort, key=lambda x: int(x[1]), reverse=True)
    return data_sort


def take_skills(main_data):
    data = []
    data_dict = {}
    for skills in map(lambda x: x['key_skills'], main_data):
        for skill in skills:
            if skill not in data_dict:
                data_dict[skill] = 1
            else:
                data_dict[skill] += 1
    for skill in data_dict:
        data.append([skill, data_dict[skill]])
    return sorted(data, key=lambda x: x[1], reverse=True)


def take_RUR(main_data):
    return list(filter(lambda x: x['salary_currency'] == "RUR", main_data))


def salary_sort(main_data, reverse=True):
    data = []
    data_sal = []
    for i, row in enumerate(main_data):
        data_sal.append([row['salary_average'], i])
    print(data_sal)
    data_sal = sorted(data_sal, key=lambda x: int(x[0]), reverse=reverse)
    for row in data_sal:
        data.append(main_data[row[1]])

    return data


def read_file(name):
    flag = True
    counter = 0
    data = []
    with open(name, encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        heading = next(reader)
        data.append(heading)
        for row in reader:
            for piece in row:
                if len(piece) == 0:
                    flag = False
                counter += 1
            if flag and (len(heading) == counter):
                data.append(row)
            flag = True
            counter = 0
    return data


def clean_data(data):
    pattern = re.compile('<.*?>')
    pattern1 = re.compile('\s+')
    heading = data[0]
    data.pop(0)
    data_new = []
    for row in data:
        dict_new = {}
        for i in range(0, len(heading)):
            if heading[i] == 'key_skills':
                dict_new[heading[i]] = row[i].split("\n")
            else:
                row[i] = row[i].replace("\n", ", ")
                row[i] = re.sub(pattern, '', row[i])
                row[i] = re.sub(pattern1, ' ', row[i])
                row[i] = row[i].strip()
                dict_new[heading[i]] = row[i]
        dict_new['salary_average'] = math.floor(
            (int(dict_new['salary_from'].replace('.0', '')) + int(dict_new['salary_to'].replace('.0', ''))) / 2)
        data_new.append(dict_new)
    return data_new


data = read_file(input())  # input()
data = clean_data(data)
data = take_RUR(data)

print_data(salary_sort(data), salary_sort(data, False), take_skills(data), take_area(data))


def printFitstGraph():
    cities = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Казань', 'Краснодар', 'Челябинск',
              'Самара', 'Пермь', 'Нижний Новгород']

    salaries = [76970, 65286, 62254, 60962, 52580, 51644, 51265, 50944, 48089, 47662]

    labels = cities
    x = np.arange(len(cities))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects2 = ax.bar(x + width / 2, salaries, width, label='Средняя з/п по городам', color='#6dee6d')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.axes.get_xaxis().set_ticks([])
    ax.set_title('Динамика уровеня зарплат по городам')
    ax.tick_params(axis='y', labelsize=8)
    ax.set_xticks(x, labels, fontsize=8, rotation=90)
    ax.legend(fontsize=11)
    ax.yaxis.grid(True)
    fig.tight_layout()

    plt.show()

def printSecondGraph():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np

    labels = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Казань', 'Нижний Новгород', 'Ростов-на-Дону', 'Екатеринбург',
              'Краснодар', 'Самара', 'Воронеж']

    sizes = [32.46, 11.97, 2.71, 2.37, 2.32, 2.09, 2.07, 1.85, 1.43, 1.41]
    print(sum(sizes))

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels)
    plt.show()

    plt.show()
