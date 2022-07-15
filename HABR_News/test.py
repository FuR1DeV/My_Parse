a = '/companies/pik-arenda'.split("?")
b = "/resumes?city_ids%5B%5D=698".split("=")[-1]
d = '\u200bКазань • Готов к удалённой работе'.split(" ")[0]
res = {}
c = {
    "list": [
            {
            "id": "andrey-sinichkin95",
            "title": "Андрей Синичкин",
            "href": "/andrey-sinichkin95",
            "conversationHref": 'null',
            "avatar": {
                "src": "https://habrastorage.org/getpro/moikrug/uploads/user/100/037/619/2/avatar/medium_7fc5deee9120420181bc0a006fafb969.jpg",
                "src2x": "https://habrastorage.org/getpro/moikrug/uploads/user/100/037/619/2/avatar/medium_7fc5deee9120420181bc0a006fafb969.jpg"
            },
            "lastVisited": {
                "title": "сегодня",
                "date": "2022-06-08T17:45:37+03:00"
            },
            "specialization": ".net разработчик",
            "qualification": {
                "title": "Senior",
                "value": 5
            },
            "salary": {
                "title": "От 250 000 ₽",
                "value": 250000,
                "currency": "rur"
            },
            "availability": {
                "title": "Не ищу работу",
                "value": "unavailable"
            },
            "location": {
                "title": "Казань",
                "name": "",
                "href": "/resumes?city_ids%5B%5D=698",
                "value": 698
            }
        }
    ]
}

print(c['list'][0].get('location').get('title'))



