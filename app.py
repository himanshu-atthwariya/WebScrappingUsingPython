import requests
from pages.pages import Pages


page_content=requests.get("http://books.toscrape.com/").content #it has page 1
page=Pages(page_content)
lists_books=page.info_list
for page_num in range(1,page.page_count):#we start from page 2 to page_count which is 50
    page_content=requests.get(f"http://books.toscrape.com/catalogue/page-{page_num+1}.html").content
    page=Pages(page_content)
    lists_books.extend(page.info_list)
