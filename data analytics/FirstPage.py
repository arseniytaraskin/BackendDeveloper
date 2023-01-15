import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#считываем csv файл
data = pd.read_csv("vacancies_dif_currencies.csv")

#тут мы исключаем строки с незаполненными значениями
data = data[data.isnull() == False]
#data = data.dropna()

#если нужно, ограничиваем тип валюты в рублях
#data = data[data['salary_currency'] == 'RUR']

main_data = data.copy()

#здесь огранчиваем дату на году - чтобы было 2005, 2007 и так далее
main_data['published_at'] = main_data['published_at'].str[:4]

#добавляем новый столбец со средней з/п, чтобы ыбло проше потом считать зп
main_data['salary'] = (main_data['salary_from'] + main_data['salary_to'])/2

#вывод средней зп по годам для всех вакансий
def salaryAll():
    for i in range(2005, 2023):
        print(main_data['salary'].loc[main_data['published_at'] == str(i)].mean(), i)

def countAll():
    for i in range(2005, 2023):
        print(len(main_data[main_data['published_at'] == str(i)]), i)


print('Средняя зп в индустрии')
print(salaryAll())
print('Общее число вакансий в индустрии')
print(countAll())


#здесь указываем выборку данных по нашей профессии
data = data[data['name'].str.contains('backend', na=False) | data['name'].str.contains('бэкенд', na=False) |
data['name'].str.contains('back end', na=False) | data['name'].str.contains('бэк енд', na=False) |
data['name'].str.contains('django',na=False) | data['name'].str.contains('flask',na=False)]

data['published_at'] = data['published_at'].str[:4]
data['salary'] = (data['salary_from'] + data['salary_to'])/2
#вывод средней зп по годам для выбранной профессии
def salaryVac():
    for i in range(2005, 2023):
        print(data['salary'].loc[data['published_at'] == str(i)].mean(), i)
print('Средняя зп по профессии: ')
print(salaryVac())

def countVac():
    for i in range(2005, 2023):
        print(len(data[data['published_at'] == str(i)]), i)
print('Общее число вакансий по профессии:')
print(countVac())

def printFirstGraph():
    #заполняем данные исходя из представленной выше аналитике
    salary = {2007: 38916, 2008: 43646, 2009: 42492, 2010: 43846, 2011: 47451, 2012: 48243, 2013: 51510, 2014: 50658,
              2015: 52696, 2016: 62675, 2017: 60935, 2018: 58335, 2019: 69467, 2020: 73431, 2021: 82690, 2022: 91795}


    salary_vacancies = {2007: 0, 2008: 0, 2009: 0, 2010: 55000, 2011: 64375, 2012: 78208, 2013: 75850, 2014: 58125,
                   2015: 89375, 2016: 84789, 2017: 95700, 2018: 101884, 2019: 104909, 2020: 114347, 2021: 151799,
                   2022: 209010}

    labels = salary.keys()

    x = np.arange(len(salary.keys()))  # the label locations

    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()

    r1 = ax.bar(x - width / 2, salary.values(), width, label='Средняя з/п в IT', color='#adacac')

    r2 = ax.bar(x + width / 2, salary_vacancies.values(), width, label='Средняя з/п в Backend', color='#5cdced')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.axes.get_xaxis().set_ticks([])

    ax.set_title('Динамика уровеня зарплат по годам')

    ax.tick_params(axis='y', labelsize=8)

    ax.set_xticks(x, labels, fontsize=8, rotation=90)

    ax.legend(fontsize=11)

    ax.yaxis.grid(True)

    fig.tight_layout()

    plt.show()

def printSecondGraph():
    n = {2005: 16022, 2006: 33321, 2007: 53562, 2008: 75070, 2009: 52889, 2010: 93494, 2011: 142458, 2012: 173897,
         2013: 234019, 2014: 259571, 2015: 284763, 2016: 332460, 2017: 391464, 2018: 517670, 2019: 535956, 2020: 489472,
         2021: 287915, 2022: 91142}

    q_name = {2005: 0, 2006: 0, 2007: 0, 2008: 0, 2009: 0, 2010: 11, 2011: 9, 2012: 32, 2013: 66, 2014: 82, 2015: 205,
              2016: 393, 2017: 597, 2018: 976, 2019: 1087, 2020: 1046, 2021: 607, 2022: 223}

    labels = n.keys()
    x = np.arange(len(n.keys()))  # the label locations
    width = 0.35  # the width of the bars

    fig, (ax, ax_1) = plt.subplots(nrows=2, ncols=1)
    r1 = ax.bar(x - width / 2, n.values(), width, color='grey')

    r1 = ax_1.bar(x - width / 2, q_name.values(), width, color='#5cdced')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.axes.get_xaxis().set_ticks([])
    ax.set_title('Динамика количества вакансий в IT')
    ax.tick_params(axis='y', labelsize=8)
    ax.set_xticks(x, labels, fontsize=8, rotation=90)

    ax.yaxis.grid(True)

    ax_1.axes.get_xaxis().set_ticks([])
    ax_1.set_title('Динамика количества вакансий в Backend')
    ax_1.tick_params(axis='y', labelsize=8)
    ax_1.set_xticks(x, labels, fontsize=8, rotation=90)

    ax_1.yaxis.grid(True)

    fig.tight_layout()

    plt.show()


