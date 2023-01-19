from tech_news.database import search_news


# Requisito 6
def search_by_title(title: str) -> list:
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    news_title_url = []

    for news in news_list:
        news_title_url.append((news["title"], news["url"]))
    return news_title_url


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
