import asyncio
import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text
from config import token, user_id
from main import check_new_jobs

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["All jobs", "Last 5 jobs", "Fresh jobs"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Jobs feed", reply_markup=keyboard)


@dp.message_handler(Text(equals="All jobs"))
async def get_all_jobs(message: types.Message):
    with open("jobs_dict.json", encoding='utf-8') as file:
        jobs_dict = json.load(file)
    for k, v in sorted(jobs_dict.items()):
        jobs = f"{hbold(v['job_title'])}\n" \
               f"{v['job_href']}\n" \
               f"{v['job_description']}"
        await message.answer(jobs)


@dp.message_handler(Text(equals="Last 5 jobs"))
async def get_last_five_jobs(message: types.Message):
    with open("jobs_dict.json", encoding='utf-8') as file:
        jobs_dict = json.load(file)
    for k, v in sorted(jobs_dict.items())[-5:]:
        jobs = f"{hbold(v['job_title'])}\n" \
               f"{v['job_href']}\n" \
               f"{v['job_description']}"
        await message.answer(jobs)


@dp.message_handler(Text(equals="Fresh jobs"))
async def get_fresh_jobs(message: types.Message):
    fresh_jobs = check_new_jobs()
    if len(fresh_jobs) >= 1:
        for k, v in sorted(fresh_jobs.items()):
            jobs = f"{hbold(v['job_title'])}\n" \
                   f"{v['job_href']}\n" \
                   f"{v['job_description']}"
            await message.answer(jobs)
    else:
        await message.answer("No jobs yet =(")


async def news_every_minute():
    keyswords = ['парс', 'телег', 'бот']
    while True:
        fresh_jobs = check_new_jobs()
        if len(fresh_jobs) >= 1:
            for k, v in sorted(fresh_jobs.items()):
                title = v['job_title']
                for i in keyswords:
                    if i in title:
                        jobs = f"{hbold(title)}\n" \
                            f"{v['job_href']}\n" \
                            f"{v['job_description']}"
                        await bot.send_message(user_id, jobs, disable_notification=True)
                    break
        await asyncio.sleep(20)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(news_every_minute())
    executor.start_polling(dp)
