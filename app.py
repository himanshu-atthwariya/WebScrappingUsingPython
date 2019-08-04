import requests
from bs4 import BeautifulSoup
from locators.listlocator import LocateLists

page_content=requests.get("http://books.toscrape.com/").content
list=LocateLists(page_content)