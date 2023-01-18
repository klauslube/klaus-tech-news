import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url: str) -> str:
    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        time.sleep(1)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError):
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content: str) -> list:
    selector = Selector(html_content)
    html_content = selector.css(".cs-overlay-link::attr(href)").getall()
    return html_content


# Requisito 3
def scrape_next_page_link(html_content: str):
    selector = Selector(html_content)
    next_page_url = selector.css("a.next::attr(href)").get()
    return next_page_url


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)
    return {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": "".join(selector.css("h1.entry-title ::text").get()).strip(),
        "timestamp": selector.css("li.meta-date ::text").get(),
        "writer": selector.css(".meta-author a::text").get(),
        "comments_count": len(selector.css("ol.comment-list li").getall())
        or 0,
        "summary": "".join(selector.css(
            ".entry-content > p:first-of-type *::text").getall()).strip(),
        "tags": selector.css("a[rel=tag] ::text").getall(),
        "category": selector.css(".label ::text").get(),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
