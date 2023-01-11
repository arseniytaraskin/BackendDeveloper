import datetime
from .models import Vacancy
import requests


def add_vacancies():
    set_vacancyModels(get_vacancies())


def set_vacancyModels(vacancies):
    models_hh_id = [item.hh_id for item in Vacancy.objects.all()]
    for vacancy in vacancies:
        if vacancy['id'] not in models_hh_id:
            model = Vacancy(
                hh_id=vacancy['id'],
                name=vacancy['name'],
                published_at=vacancy['published_at'],
                description=vacancy['description'],
                key_skills=vacancy['key_skills'],
                address=vacancy['area'] if vacancy['address'] is None else vacancy['address']['city'],
                url=vacancy['alternate_url'],
                employer=vacancy['employer']['name'],
                salary=vacancy['salary'], )
            model.save()


def clean_vacancy(vacancy):
    vacancy['area'] = vacancy['area']['name'] if vacancy['area'].__contains__('name') else 'Нет данных'
    if vacancy['salary']['from'] != None and vacancy['salary']['to'] != None and vacancy['salary']['from'] != \
            vacancy['salary']['to']:
        vacancy[
            'salary'] = f"от {'{0:,}'.format(vacancy['salary']['from']).replace(',', ' ')} до {'{0:,}'.format(vacancy['salary']['to']).replace(',', ' ')} {vacancy['salary']['currency']}"
    elif vacancy['salary']['from'] != None:
        vacancy[
            'salary'] = f"{'{0:,}'.format(vacancy['salary']['from']).replace(',', ' ')} {vacancy['salary']['currency']}"
    elif vacancy['salary']['to'] != None:
        vacancy[
            'salary'] = f"{'{0:,}'.format(vacancy['salary']['to']).replace(',', ' ')} {vacancy['salary']['currency']}"
    else:
        vacancy['salary'] = 'Нет данных'
    vacancy['key_skills'] = ', '.join(map(lambda x: x['name'], vacancy['key_skills']))
    return vacancy


def get_api():
    params = {
        'text': 'backend',
        'specialization': 1,
        'page': 1,
        'per_page': 100,
    }
    return requests.get('https://api.hh.ru/vacancies', params).json()


def get_vacancies():
    try:
        data = []
        info = get_api()
        for row in info['items']:
            if row['name'].lower().__contains__('backend') and not row['salary'] is None:
                data.append({'id': row['id'], 'published_at': row['published_at']})
        data = sorted(data, key=lambda x: x['published_at'])
        vacancies = []
        for vacancy in data[len(data) - 10:]:
            vacancies.append(clean_vacancy(requests.get(f'https://api.hh.ru/vacancies/{vacancy["id"]}').json()))
        return vacancies
    except Exception as e:
        print(e)
        print(datetime.datetime.now())
        return []


if __name__ == "__main__":
    add_vacancies()