# 2) Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой больше введенной суммы

from scrapingjob import ScrapingJob
from pprint import pprint

vacancy_db = ScrapingJob('mongodb://172.17.0.2:27017/', 'vacancy', 'vacancy_db')
vacancy_db.print_salary(300_000)

# 3)Написать функцию, которая будет добавлять в вашу базу данных только новые вакансии с сайта

vacancy_db.collection.update_one({'vacancy_link': 'https://hh.ru/vacancy/31828023'},
                                 {'$set': {'city':'Москва', 'company_name':'some compary'}})
objects = vacancy_db.collection.find().limit(1)
for obj in objects:
    pprint(obj)

vacancy = 'Python'
vacancy_db.search_job(vacancy)

objects = vacancy_db.collection.find().limit(1)
for obj in objects:
    pprint(obj)


