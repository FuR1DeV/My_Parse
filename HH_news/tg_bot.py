import asyncio
import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text
from HH_news.config import token, user_id
from HH_news.main import check_fresh_site_news, check_fresh_market_news, check_fresh_articles

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def hi(message: types.Message):
    buttons = ["Все новости сайта", "Свежие новости сайта",
               "Все новости рынка", "Свежие новости рынка",
               "Все статьи", "Свежие статьи"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    await message.answer("Новости и статьи портала Head Hunter", reply_markup=keyboard)


# Новости сайта
@dp.message_handler(Text(equals="Все новости сайта"))
async def all_news(message: types.Message):
    with open("news_dict.json", encoding='utf-8') as file:
        news_dict = json.load(file)
    for k, v in sorted(news_dict.items()):
        news = f"{hbold(v['news_title'])}\n" \
               f"{v['news_url']}\n"
        await message.answer(news)
    await message.answer(f"Количество новостей сайта - {len(news_dict)}")


# Свежие новости сайта
@dp.message_handler(Text(equals="Свежие новости сайта"))
async def fresh_news(message: types.Message):
    await message.answer("Нужно немножко подождать...")
    fresh_news = check_fresh_site_news()
    if len(fresh_news) >= 1:
        for k, v in sorted(fresh_news.items()):
            news = f"{hbold(v['news_title'])}\n" \
                   f"{v['news_url']}\n"
            await message.answer(news)
        await message.answer(f"Количество свежих новостей сайта - {len(fresh_news)}")
    else:
        await message.answer('Свежих новостей сайта нет...')


# Все новости рынка
@dp.message_handler(Text(equals="Все новости рынка"))
async def all_news(message: types.Message):
    with open("market_news_dict.json", encoding='utf-8') as file:
        market_news_dict = json.load(file)
    for k, v in sorted(market_news_dict.items()):
        news = f"{hbold(v['market_news_title'])}\n" \
               f"{v['market_news_url']}\n"
        await message.answer(news)
    await message.answer(f"Количество новостей рынка - {len(market_news_dict)}")


# Свежие новости рынка
@dp.message_handler(Text(equals="Свежие новости рынка"))
async def fresh_news(message: types.Message):
    await message.answer("Нужно немножко подождать...")
    fresh_market_news = check_fresh_market_news()
    if len(fresh_market_news) >= 1:
        for k, v in sorted(fresh_market_news.items()):
            market_news = f"{hbold(v['market_news_title'])}\n" \
                   f"{v['market_news_url']}\n"
            await message.answer(market_news)
        await message.answer(f"Количество свежих новостей рынка - {len(fresh_market_news)}")
    else:
        await message.answer('Свежих новостей рынка нет...')


# Все статьи
@dp.message_handler(Text(equals="Все статьи"))
async def all_news(message: types.Message):
    with open("articles_dict.json", encoding='utf-8') as file:
        articles_dict = json.load(file)
    for k, v in sorted(articles_dict.items()):
        article = f"{hbold(v['article_title'])}\n" \
               f"{v['article_url']}\n"
        await message.answer(article)
    await message.answer(f"Количество статей - {len(articles_dict)}")


# Свежие статьи
@dp.message_handler(Text(equals="Свежие статьи"))
async def fresh_news(message: types.Message):
    await message.answer("Нужно немножко подождать...")
    articles_news = check_fresh_articles()
    if len(articles_news) >= 1:
        for k, v in sorted(articles_news.items()):
            article_news = f"{hbold(v['article_title'])}\n" \
                   f"{v['article_url']}\n"
            await message.answer(article_news)
        await message.answer(f"Количество свежих статей - {len(articles_news)}")
    else:
        await message.answer('Свежих статей нет...')


if __name__ == '__main__':
    #loop = asyncio.get_event_loop()
    #loop.create_task(news_every_minute())
    executor.start_polling(dp)
