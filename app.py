import requests
from pages.Pages import Pages

page_content=requests.get("http://books.toscrape.com/").content
page=Pages(page_content)
lists_books=page.info_list