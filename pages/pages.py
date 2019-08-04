import re
from bs4 import BeautifulSoup
from parsers.listParser import ListParser
from locators.locator import Locator
"""
In takes the entire html content and parse it with BeautiulSoup
"""
class Pages:
    def __init__(self,page_content):
        self.soup=BeautifulSoup(page_content,"html.parser")

    @property
    def info_list(self):
        locator=Locator.LIST_LOCATOR
        lists=self.soup.select(locator)
        info=[]#u can use list compression also
        for list in lists:
            info.append(ListParser(list))
        return info

    @property
    def page_count(self):
        locator=Locator.PAGE_NUM_LOCATOR
        pages=self.soup.select_one(locator).string
        pattern="[A-z]+ [0-9]+ [A-z]+ ([0-9]+)" #Page 1 of 50
        matcher=re.search(pattern,pages)
        return int(matcher.group(1))
