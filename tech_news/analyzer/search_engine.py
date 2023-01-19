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
        date_format = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        query = {"timestamp": {"$eq": date_format}}
        formated_list = []

        for new in search_news(query):
            formated_list.append((new["title"], new["url"]))
        return formated_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    news_list = search_news({"tags": {"$regex": tag, "$options": "i"}})
    tag_list = []
    for news in news_list:
        tag_list.append((news["title"], news["url"]))
    return tag_list


# Requisito 9
def search_by_category(category):
    news_list = search_news({"category": {"$regex": category, "$options": "i"}})
    category_list = []
    for news in news_list:
        category_list.append((news["title"], news["url"]))
    return category_list
