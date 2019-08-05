import requests
import logging
from pages.pages import Pages

logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
                    datefmt="%d-%m-%Y %H:%M:%S",
                    level=logging.INFO,
                    filename="logs.txt")
logger=logging.getLogger("scraping")
logger.info("Loading books list....")

page_content=requests.get("http://books.toscrape.com/").content #it has page 1
page=Pages(page_content)
lists_books=page.info_list
for page_num in range(1,page.page_count):#we start from page 2 to page_count which is 50
    page_content=requests.get(f"http://books.toscrape.com/catalogue/page-{page_num+1}.html").content
    logger.debug("Creating All Pages from page content")
    page=Pages(page_content)
    lists_books.extend(page.info_list)
