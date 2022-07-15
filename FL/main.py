import json

import requests
from bs4 import BeautifulSoup


def get_jobs():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.45"
    }
    jobs_dict = {}

    url = f"https://www.fl.ru/projects/category/programmirovanie/"
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    jobs = soup.find_all("div", id="projects-list")
    for v in jobs:
        res = v.find_all("h2", class_="b-post__title")
        for i in res:
            url_job = f"https://www.fl.ru{i.find('a').get('href')}"
            r = requests.get(url=url_job, headers=headers)
            soup = BeautifulSoup(r.text, "html.parser")
            id = i.find("a").get("name")[3:]
            id_project = f'projectp{i.find("a").get("name")[3:]}'
            jobs_in = soup.find("div", id=id_project)
            jobs_dict[id] = {
                "job_href": url_job,
                "job_title": i.find("a").text,
                "job_description": jobs_in.text.strip(),
            }
            print(len(jobs_dict))
    with open("jobs_dict.json", "w", encoding='utf-8') as file:
        json.dump(jobs_dict, file, indent=4, ensure_ascii=False)


def check_new_jobs():
    with open('jobs_dict.json', encoding='utf-8') as file:
        jobs_dict = json.load(file)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.45"
    }
    url = f"https://www.fl.ru/projects/category/programmirovanie/"
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    jobs = soup.find_all("div", id="projects-list")
    new_jobs = {}
    for v in jobs:
        res = v.find_all("h2", class_="b-post__title")
        for i in res:
            id = i.find("a").get("name")[3:]
            if id in jobs_dict:
                continue
            else:
                url_job = f"https://www.fl.ru{i.find('a').get('href')}"
                r = requests.get(url=url_job, headers=headers)
                soup = BeautifulSoup(r.text, "html.parser")
                id_project = f'projectp{i.find("a").get("name")[3:]}'
                jobs_in = soup.find("div", id=id_project)
                # Добавим в прежний словарь
                jobs_dict[id] = {
                    "job_href": url_job,
                    "job_title": i.find("a").text,
                    "job_description": jobs_in.text.strip(),
                }
                # Добавим в свежий словарь
                new_jobs[id] = {
                    "job_href": url_job,
                    "job_title": i.find("a").text,
                    "job_description": jobs_in.text.strip(),
                }

    with open("jobs_dict.json", "w", encoding='utf-8') as file:
        json.dump(jobs_dict, file, indent=4, ensure_ascii=False)

    return new_jobs


def main():
    # get_jobs()
    check_new_jobs()


if __name__ == '__main__':
    main()
