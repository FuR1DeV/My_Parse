import asyncio
import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text
from HH.config import token, user_id
from HH.main import check_new_vacancies

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def hi(message: types.Message):
    buttons = ["Все вакансии", "Свежие вакансии"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    await message.answer("Вакансии Python junior", reply_markup=keyboard)


@dp.message_handler(Text(equals="Все вакансии"))
async def all_vacancies(message: types.Message):
    with open("jobs_dict.json", encoding='utf-8') as file:
        jobs_dict = json.load(file)
    for k, v in sorted(jobs_dict.items()):
        jobs = f"{hbold(v['job_title'])}\n" \
               f"{v['job_money']}\n" \
               f"{v['employer_name']}\n" \
               f"{v['city']}\n" \
               f"{v['job_desc']}\n" \
               f"{v['job_requirement']}\n" \
               f"{v['job_url']}"
        await message.answer(jobs)
    await message.answer(f"Количество вакансий - {len(jobs_dict)}")


@dp.message_handler(Text(equals="Свежие вакансии"))
async def fresh_vacancies(message: types.Message):
    await message.answer("Нужно немножко подождать...")
    new_jobs = check_new_vacancies()
    if len(new_jobs) >= 1:
        for k, v in sorted(new_jobs.items()):
            jobs = f"{hbold(v['job_title'])}\n" \
                   f"{v['job_money']}\n" \
                   f"{v['employer_name']}\n" \
                   f"{v['city']}\n" \
                   f"{v['job_desc']}\n" \
                   f"{v['job_requirement']}\n" \
                   f"{v['job_url']}"
            await message.answer(jobs)
        await message.answer(f"Количество новых вакансий - {len(new_jobs)}")
    else:
        await message.answer('Новых вакансий нет...')


@dp.message_handler(commands="check_length")
async def check_length(message: types.Message):
    with open("jobs_dict.json", encoding='utf-8') as file:
        jobs_dict = json.load(file)
    await message.answer(f"Количество вакансий - {len(jobs_dict)}")


if __name__ == '__main__':
    #loop = asyncio.get_event_loop()
    #loop.create_task(news_every_minute())
    executor.start_polling(dp)
