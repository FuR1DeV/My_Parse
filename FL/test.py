a = "https://www.fl.ru/projects/5002315/vnesti-izmeneniya-v-gotovyiy-proekt-na-aspnet.html"

print(a.split("/")[4])

keyswords = ['парс', 'телег', 'бот']

title = 'Написать софт парсер на python, а потом сделать бота в телеге'

for i in keyswords:
    if i in title:
        print('YES')
    else:
        print('NO')
