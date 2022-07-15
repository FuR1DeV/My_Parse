import json

import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_site_news():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.75"
    }
    news_dict = {}
    for i in range(0, 5, 1):
        url = f'https://hh.ru/articles/site-news?page={i}'
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, "lxml")
        news = soup.find("div", class_="cms-announce-tiles")
        for new in news:
            news_url = f'https://hh.ru/article/{(new.get("href")).split("/")[:][-1]}'
            news_id = new.get("href").split("/")[:][-1]
            news_title = new.find("span").text.strip()
            news_img_url = new.find("img").get("src")
            news_dict[news_id] = {
                'news_url': news_url,
                'news_id': news_id,
                'news_title': news_title,
                'news_img_url': news_img_url,
            }
    with open("news_dict.json", "w", encoding='utf-8') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)


def check_fresh_site_news():
    with open('news_dict.json', encoding='utf-8') as file:
        news_dict = json.load(file)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.75"
    }
    fresh_news = {}
    for i in range(0, 5, 1):
        url = f'https://hh.ru/articles/site-news?page={i}'
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, "lxml")
        news = soup.find("div", class_="cms-announce-tiles")
        for new in news:
            news_url = f'https://hh.ru/article/{(new.get("href")).split("/")[:][-1]}'
            news_id = new.get("href").split("/")[:][-1]
            if news_id in news_dict:
                continue
            else:
                news_title = new.find("span").text.strip()
                news_img_url = new.find("img").get("src")
                news_dict[news_id] = {
                    'news_url': news_url,
                    'news_id': news_id,
                    'news_title': news_title,
                    'news_img_url': news_img_url,
                }
                fresh_news[news_id] = {
                    'news_url': news_url,
                    'news_id': news_id,
                    'news_title': news_title,
                    'news_img_url': news_img_url,
                }
    with open("news_dict.json", "w", encoding='utf-8') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)
    print(len(fresh_news))
    return fresh_news


def get_market_news():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.75"
    }
    market_news_dict = {}
    for i in range(0, 5, 1):
        url = f'https://hh.ru/articles/market-news?page={i}'
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, "lxml")
        market_news = soup.find("div", class_="cms-announce-tiles")
        for new in market_news:
            market_news_url = f'https://hh.ru/article/{(new.get("href")).split("/")[:][-1]}'
            market_news_id = new.get("href").split("/")[:][-1]
            market_news_title = new.find("span").text.strip()
            market_news_img_url = new.find("img").get("src")
            market_news_dict[market_news_id] = {
                'market_news_url': market_news_url,
                'market_news_id': market_news_id,
                'market_news_title': market_news_title,
                'market_news_img_url': market_news_img_url,
            }
    with open("market_news_dict.json", "w", encoding='utf-8') as file:
        json.dump(market_news_dict, file, indent=4, ensure_ascii=False)


def check_fresh_market_news():
    with open('market_news_dict.json', encoding='utf-8') as file:
        market_news_dict = json.load(file)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.75"
    }
    fresh_market_news = {}
    for i in range(0, 5, 1):
        url = f'https://hh.ru/articles/market-news?page={i}'
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, "lxml")
        market_news = soup.find("div", class_="cms-announce-tiles")
        for new in market_news:
            market_news_url = f'https://hh.ru/article/{(new.get("href")).split("/")[:][-1]}'
            market_news_id = new.get("href").split("/")[:][-1]
            if market_news_id in market_news_dict:
                continue
            else:
                market_news_title = new.find("span").text.strip()
                market_news_img_url = new.find("img").get("src")
                market_news_dict[market_news_id] = {
                    'market_news_url': market_news_url,
                    'market_news_id': market_news_id,
                    'market_news_title': market_news_title,
                    'market_news_img_url': market_news_img_url,
                }
                fresh_market_news[market_news_id] = {
                    'market_news_url': market_news_url,
                    'market_news_id': market_news_id,
                    'market_news_title': market_news_title,
                    'market_news_img_url': market_news_img_url,
                }
    with open("market_news_dict.json", "w", encoding='utf-8') as file:
        json.dump(market_news_dict, file, indent=4, ensure_ascii=False)
    print(len(fresh_market_news))
    return fresh_market_news


def get_articles():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.75"
    }
    articles_dict = {}
    url = 'https://hh.ru/articles'
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    articles = soup.find("div", class_="cms-announce-tiles_underlined")
    for article in articles:
        article_url = f'https://hh.ru/article/{(article.get("href")).split("/")[:][-1]}'
        article_id = article.get("href").split("/")[:][-1]
        article_title = article.find("span").text.strip()
        article_img_url = article.find("img").get("src")
        articles_dict[article_id] = {
            'article_url': article_url,
            'article_id': article_id,
            'article_title': article_title,
            'article_img_url': article_img_url,
        }
    with open("articles_dict.json", "w", encoding='utf-8') as file:
        json.dump(articles_dict, file, indent=4, ensure_ascii=False)


def check_fresh_articles():
    with open('articles_dict.json', encoding='utf-8') as file:
        articles_dict = json.load(file)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.75"
    }
    url = 'https://hh.ru/articles'
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    articles = soup.find("div", class_="cms-announce-tiles_underlined")
    fresh_articles = {}
    for article in articles:
        article_url = f'https://hh.ru/article/{(article.get("href")).split("/")[:][-1]}'
        article_id = article.get("href").split("/")[:][-1]
        if article_id in articles_dict:
            continue
        else:
            article_title = article.find("span").text.strip()
            article_img_url = article.find("img").get("src")
            articles_dict[article_id] = {
                'article_url': article_url,
                'article_id': article_id,
                'article_title': article_title,
                'article_img_url': article_img_url,
            }
            fresh_articles[article_id] = {
                'article_url': article_url,
                'article_id': article_id,
                'article_title': article_title,
                'article_img_url': article_img_url,
            }
    with open("articles_dict.json", "w", encoding='utf-8') as file:
        json.dump(articles_dict, file, indent=4, ensure_ascii=False)
    print(len(fresh_articles))
    return fresh_articles


def main():
    #get_site_news()
    #print(check_fresh_site_news())
    #get_market_news()
    #print(check_fresh_market_news())
    #get_articles()
    print(check_fresh_articles())


if __name__ == '__main__':
    main()
