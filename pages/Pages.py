from bs4 import BeautifulSoup
from parsers.ListParser import ListParser
from locators.listLocator import ListLocator
"""
In takes the entire html content and parse it with BeautiulSoup
"""
class Pages:
    def __init__(self,page_content):
        self.soup=BeautifulSoup(page_content,"html.parser")

    @property
    def info_list(self):
        locator=ListLocator.LIST_LOCATOR
        lists=self.soup.select(locator)
        info=[]#u can use list compression also
        for list in lists:
            info.append(ListParser(list))
        return info