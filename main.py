import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

HOST = 'https://spb.hh.ru/search/vacancy?text=python+Django+Flask&salary=&area=1&area=2&ored_clusters=true&enable_snippets=true'

def get_headers():
    headers = Headers(browser='firefox', os='win')
    return headers.generate()

hh = requests.get(HOST, headers=get_headers())
hh_python = hh.text

# print(hh_python)
soup = BeautifulSoup(hh_python, features='lxml')

hh = soup.find_all('div', class_='serp-item')

# print(hh)

for prof in hh:
    # print(prof)
    href_a = prof.find('a')
    href = href_a['href']
    # print(href)

    salary_span = prof.find('span', class_='bloko-header-section-3')
    print(salary_span)
    salary_num = salary_span.text
    print(salary_num)

#     serp_item_title = soup.find('div', class_='serp-item__title')
#     print(serp_item_title)
#     prof_text = prof.text
#     print(prof_text)
    # href = prof_text.find('href')
    # print(prof)
# print(serp_item)
# vacancy_serp_content = soup.find('div', class_='vacancy-serp-content')
# serp_item = vacancy_serp_content.find_all('serp-item')
# print(serp_item)

# print(vacancy_serp_content)
# print(serp_item)
# serp_item_title = soup.find_all('a', class_='serp-item__title')
# print(serp_item_title)

# for prof in serp_item_title:
#     # header = prof.find('a')
#     title = prof.text
#     href = prof['href']
#
#     # href = prof.find['href']
#     print(href)

# hh_link = hh_articles.find('a')
# print(serp_item_title)

