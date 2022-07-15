import json

import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_vacancies():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.75"
    }
    jobs_dict = {}
    for page in range(0, 10, 1):
        url = f"https://hh.ru/search/vacancy?area=1&fromSearchLine=true&text=python+junior&page={page}&hhtmFrom=vacancy_search_list"
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, "lxml")
        jobs = soup.find_all("div", class_="vacancy-serp-item__layout")
        for job in jobs:
            try:
                job_url = job.find("a", class_="bloko-link").get("href").split('?')[:-1][-1]
                job_id = job_url.split('/')[:][-1]
                job_title = job.find("a", class_="bloko-link").text.strip()
                job_money = job.find("span", class_="bloko-header-section-3").text.strip().replace(u"\u202f", " ")
                employer_url = f'https://hh.ru{job.find("a", class_="bloko-link_kind-tertiary").get("href").split("?")[:-1][-1]}'
                employer_name = job.find("a", class_="bloko-link_kind-tertiary").text.strip().replace(u"\u00A0", " ")
                city = job.find("div", class_="bloko-text_no-top-indent").text.strip().replace(u"\u00A0", " ")
                try:
                    job_desc = job.find_all(attrs={"data-qa": "vacancy-serp__vacancy_snippet_responsibility"})[0].text.strip()
                except IndexError:
                    job_desc = 'Описание отсутствует'
                try:
                    job_requirement = job.find_all(attrs={"data-qa": "vacancy-serp__vacancy_snippet_requirement"})[0].text.strip()
                except IndexError:
                    job_requirement = 'Требования отсутствуют'
                jobs_dict[job_id] = {
                    'job_url': job_url,
                    'job_id': job_id,
                    'job_title': job_title,
                    'job_money': job_money,
                    'employer_name': employer_name,
                    'employer_url': employer_url,
                    'city': city,
                    'job_desc': job_desc,
                    'job_requirement': job_requirement,

                }
            except AttributeError:

                job_url = job.find("a", class_="bloko-link").get("href").split('?')[:-1][-1]
                job_id = job_url.split('/')[:][-1]
                job_title = job.find("a", class_="bloko-link").text.strip()
                job_money = 'з/п не указана'
                employer_url = f'https://hh.ru{job.find("a", class_="bloko-link_kind-tertiary").get("href").split("?")[:-1][-1]}'
                employer_name = job.find("a", class_="bloko-link_kind-tertiary").text.strip().replace(u"\u00A0", " ")
                city = job.find("div", class_="bloko-text_no-top-indent").text.strip().replace(u"\u00A0", " ")
                try:
                    job_desc = job.find_all(attrs={"data-qa": "vacancy-serp__vacancy_snippet_responsibility"})[0].text.strip()
                except IndexError:
                    job_desc = 'Описание отсутствует'
                try:
                    job_requirement = job.find_all(attrs={"data-qa": "vacancy-serp__vacancy_snippet_requirement"})[0].text.strip()
                except IndexError:
                    job_requirement = 'Требования отсутствуют'
                jobs_dict[job_id] = {
                    'job_url': job_url,
                    'job_id': job_id,
                    'job_title': job_title,
                    'job_money': job_money,
                    'employer_name': employer_name,
                    'employer_url': employer_url,
                    'city': city,
                    'job_desc': job_desc,
                    'job_requirement': job_requirement,
                }

    with open("jobs_dict.json", "w", encoding='utf-8') as file:
        json.dump(jobs_dict, file, indent=4, ensure_ascii=False)
    print(len(jobs_dict))


def check_new_vacancies():
    with open('jobs_dict.json', encoding='utf-8') as file:
        jobs_dict = json.load(file)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.75"
    }
    fresh_job = {}
    for page in range(0, 10, 1):
        url = f"https://hh.ru/search/vacancy?area=1&fromSearchLine=true&text=python+junior&page={page}&hhtmFrom=vacancy_search_list"
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, "lxml")
        jobs = soup.find_all("div", class_="vacancy-serp-item__layout")
        for job in jobs:
            job_url = job.find("a", class_="bloko-link").get("href").split('?')[:-1][-1]
            job_id = job_url.split('/')[:][-1]

            if job_id in jobs_dict:
                continue
            else:
                try:
                    job_title = job.find("a", class_="bloko-link").text.strip()
                    job_money = job.find("span", class_="bloko-header-section-3").text.strip().replace(u"\u202f", " ")
                    employer_url = f'https://hh.ru{job.find("a", class_="bloko-link_kind-tertiary").get("href").split("?")[:-1][-1]}'
                    employer_name = job.find("a", class_="bloko-link_kind-tertiary").text.strip().replace(u"\u00A0", " ")
                    city = job.find("div", class_="bloko-text_no-top-indent").text.strip().replace(u"\u00A0", " ")
                    try:
                        job_desc = job.find_all(attrs={"data-qa": "vacancy-serp__vacancy_snippet_responsibility"})[0].text.strip()
                    except IndexError:
                        job_desc = 'Описание отсутствует'
                    try:
                        job_requirement = job.find_all(attrs={"data-qa": "vacancy-serp__vacancy_snippet_requirement"})[0].text.strip()
                    except IndexError:
                        job_requirement = 'Требования отсутствуют'
                    jobs_dict[job_id] = {
                        'job_url': job_url,
                        'job_id': job_id,
                        'job_title': job_title,
                        'job_money': job_money,
                        'employer_name': employer_name,
                        'employer_url': employer_url,
                        'city': city,
                        'job_desc': job_desc,
                        'job_requirement': job_requirement,
                    }
                    fresh_job[job_id] = {
                        'job_url': job_url,
                        'job_id': job_id,
                        'job_title': job_title,
                        'job_money': job_money,
                        'employer_name': employer_name,
                        'employer_url': employer_url,
                        'city': city,
                        'job_desc': job_desc,
                        'job_requirement': job_requirement,
                    }
                except AttributeError:

                    job_title = job.find("a", class_="bloko-link").text.strip()
                    job_money = 'з/п не указана'
                    employer_url = f'https://hh.ru{job.find("a", class_="bloko-link_kind-tertiary").get("href").split("?")[:-1][-1]}'
                    employer_name = job.find("a", class_="bloko-link_kind-tertiary").text.strip().replace(u"\u00A0", " ")
                    city = job.find("div", class_="bloko-text_no-top-indent").text.strip().replace(u"\u00A0", " ")
                    try:
                        job_desc = job.find_all(attrs={"data-qa": "vacancy-serp__vacancy_snippet_responsibility"})[0].text.strip()
                    except IndexError:
                        job_desc = 'Описание отсутствует'
                    try:
                        job_requirement = job.find_all(attrs={"data-qa": "vacancy-serp__vacancy_snippet_requirement"})[0].text.strip()
                    except IndexError:
                        job_requirement = 'Требования отсутствуют'
                    jobs_dict[job_id] = {
                        'job_url': job_url,
                        'job_id': job_id,
                        'job_title': job_title,
                        'job_money': job_money,
                        'employer_name': employer_name,
                        'employer_url': employer_url,
                        'city': city,
                        'job_desc': job_desc,
                        'job_requirement': job_requirement,
                    }
                    fresh_job[job_id] = {
                        'job_url': job_url,
                        'job_id': job_id,
                        'job_title': job_title,
                        'job_money': job_money,
                        'employer_name': employer_name,
                        'employer_url': employer_url,
                        'city': city,
                        'job_desc': job_desc,
                        'job_requirement': job_requirement,
                    }

    with open("jobs_dict.json", "w", encoding='utf-8') as file:
        json.dump(jobs_dict, file, indent=4, ensure_ascii=False)
    print(len(fresh_job))
    print(len(jobs_dict))
    return fresh_job


def main():
    #get_vacancies()
    print(check_new_vacancies())


if __name__ == '__main__':
    main()
