import json

import requests
from bs4 import BeautifulSoup


def get_resumes():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.36"
    }
    resume_dict = {}

    url = f"https://career.habr.com/resumes"
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    resumes = soup.find_all("div", class_="resume-card__body")
    for card in resumes:
        try:
            card_id = card.find("a", class_="resume-card__title-link").get("href")
            card_title = card.find("a", class_="resume-card__title-link").text.strip()
            card_specialization = card.find("span", class_="resume-card__specialization").text.strip()
            card_offer = card.find("div", class_="resume-card__offer").text.strip()
            card_appearence = card.find_all("a", class_="link-comp link-comp--appearance-dark")
            skills_list = []
            city_id = 0
            city, company, education, university = 'Нет города', 'Нет последнего места работы', 'Нет образовательных курсов', 'Нет Университета'
            for card_app in card_appearence:
                try:
                    if card_app.get("href").split("?")[1:][-1].split('%')[0] == 'city_ids':
                        city_id = card_app.get("href").split("=")[-1]
                except:
                    pass
                try:
                    if card_app.get("href").split("?")[1:][-1].split('%')[0] == 'skills':
                        skills_list.append(card_app.string)
                except:
                    pass
                try:
                    if card_app.get("href").split("/")[1:][0] == 'companies':
                        company = card_app.string
                except:
                    pass
                try:
                    if card_app.get("href").split("/")[1:][0] == 'education_centers':
                        education = card_app.string
                except:
                    pass
                try:
                    if card_app.get("href").split("/")[1:][0] == 'universities':
                        university = card_app.string
                except:
                    pass

            card_content = card.find_all("span", class_="inline-list")
            card_content_list = []
            # print(card_content)
            # city = card.find_all(attrs={"href": f"/resumes?city_ids%5B%5D={city_id}"})
            for card_cont in card_content:
                card_content_list.append(card_cont.text.strip())
                if company in card_cont.text.strip():
                    company = card_cont.text.strip()
                try:
                    a = card.find_all("h2", class_="content-section__title")
                    for i in a:
                        if "Последнее место работы" in i:
                            company = card_content_list[5]
                except:
                    pass
            try:
                resume_dict[card_id] = {
                    "card_title": card_title,
                    "card_specialization": card_specialization,
                    "card_offer": card_offer,
                    "card_skills": ', '.join(skills_list),
                    "card_age_and_experience": card_content_list[3],
                    "card_city": card_content_list[4].replace(u"\u200b", ""),
                    "card_last_job": company,
                    "card_education": education,
                    "card_higher education": university,
                }
            except:
                print("Error in creating dict")
        except AttributeError:
            print("AttributeError")

    with open("resume_dict.json", "w", encoding='utf-8') as file:
        json.dump(resume_dict, file, indent=4, ensure_ascii=False)


def check_new_resumes():
    with open("resume_dict.json", encoding='utf-8') as file:
        resume_dict = json.load(file)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.36"
    }
    url = f"https://career.habr.com/resumes"
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    resumes = soup.find_all("div", class_="resume-card__body")
    for card in resumes:
        card_id = card.find("a", class_="resume-card__title-link").get("href")
        if card_id in resume_dict:
            continue
        else:
            try:
                card_title = card.find("a", class_="resume-card__title-link").text.strip()
                card_specialization = card.find("span", class_="resume-card__specialization").text.strip()
                card_offer = card.find("div", class_="resume-card__offer").text.strip()
                card_appearence = card.find_all("a", class_="link-comp link-comp--appearance-dark")
                skills_list = []
                city, company, education, university = 'Нет города', 'Нет последнего места работы', 'Нет образовательных курсов', 'Нет Университета'
                for card_app in card_appearence:
                    try:
                        if card_app.get("href").split("?")[1:][-1].split('%')[0] == 'skills':
                            skills_list.append(card_app.string)
                    except:
                        pass
                    try:
                        if card_app.get("href").split("/")[1:][0] == 'companies':
                            company = card_app.string
                    except:
                        pass
                    try:
                        if card_app.get("href").split("/")[1:][0] == 'education_centers':
                            education = card_app.string
                    except:
                        pass
                    try:
                        if card_app.get("href").split("/")[1:][0] == 'universities':
                            university = card_app.string
                    except:
                        pass

                card_content = card.find_all("span", class_="inline-list")
                card_content_list = []
                for card_cont in card_content:
                    card_content_list.append(card_cont.text.strip())
                    if company in card_cont.text.strip():
                        company = card_cont.text.strip()
                    try:
                        a = card.find_all("h2", class_="content-section__title")
                        for i in a:
                            if "Последнее место работы" in i:
                                company = card_content_list[5]
                    except:
                        pass
                try:
                    resume_dict[card_id] = {
                        "card_title": card_title,
                        "card_specialization": card_specialization,
                        "card_offer": card_offer,
                        "card_skills": ', '.join(skills_list),
                        "card_age_and_experience": card_content_list[3],
                        "card_city": card_content_list[4].replace(u"\u200b", ""),
                        "card_last_job": company,
                        "card_education": education,
                        "card_higher_education": university,
                    }
                except:
                    pass
            except AttributeError:
                pass
            with open("resume_dict.json", "w", encoding='utf-8') as file:
                json.dump(resume_dict, file, indent=4, ensure_ascii=False)


def get_resumes_v2():

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.36"
    }
    url = f"https://career.habr.com/api/frontend/resumes?order=last_visited&currency=RUR&city_ids[]=698"
    r = requests.get(url=url, headers=headers)

    with open(f"info.json", "w", encoding='utf-8') as file:
        json.dump(r.json(), file, indent=4, ensure_ascii=False)

    resumes = r.json()['list']
    print(resumes)


def main():
    # get_resumes()
    # check_new_resumes()
    # create_city_dict()
    get_resumes_v2()


if __name__ == '__main__':
    main()
