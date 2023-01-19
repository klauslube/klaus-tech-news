from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title: str) -> list:
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    news_title_url = []

    for news in news_list:
        news_title_url.append((news["title"], news["url"]))
    return news_title_url


# Requisito 7
def search_by_date(date):
    try:
        formated_list = []
        date_format = datetime.fromisoformat(date).strftime("%d%m%Y")
        news_list = search_news({"timestamp": {"$regex": date_format}})

        for news in news_list:
            formated_list.append((news["title"], news["url"]))
        return formated_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
