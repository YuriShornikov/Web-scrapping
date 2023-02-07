import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import json

HOST = 'https://spb.hh.ru/search/vacancy?text=python+Django+Flask&salary=&area=1&area=2&ored_clusters=true&enable_snippets=true'

data_list = []

for i in range(0, 4):
    url = HOST + '&page=' + str(i)

    def get_headers():
        headers = Headers(browser='firefox', os='win')
        return headers.generate()

    hh = requests.get(url, headers=get_headers())
    hh_python = hh.text

    # print(hh_python)
    soup = BeautifulSoup(hh_python, features='lxml')

    hh = soup.find_all('div', class_='serp-item')

    # print(hh)

    for prof in hh:
        # print(prof)
        href_code = prof.find('a')
        href = href_code['href']
        # print(href)

        salary_code = prof.find('span', class_='bloko-header-section-3')
        if salary_code == None:
            salary = ' '
        else:
            salary = salary_code.text

        #не выводит нормально зарплату

        name_code = prof.find('div', class_='vacancy-serp-item__meta-info-company')
        name = name_code.text

        city_code = prof.find('div', attrs= {'data-qa': 'vacancy-serp__vacancy-address'}, class_='bloko-text')
        city = city_code.text.split(',')


        form = {
            'href': href,
            'salary': salary,
            'company': name,
            'city': city[0]
        }
        data_list.append(form)
        # print(data_list)

with open('hh.json', 'w', encoding='utf-8') as f:
    json.dump(data_list, f, indent=5)



