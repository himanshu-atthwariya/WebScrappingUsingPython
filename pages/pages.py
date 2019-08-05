import re
import logging
from bs4 import BeautifulSoup
from parsers.listParser import ListParser
from locators.locator import Locator
"""
In takes the entire html content and parse it with BeautiulSoup
"""

logger=logging.getLogger("scrappinq.pages")


class Pages:
    def __init__(self,page_content):
        logger.debug("Parsing page content with Beautiful HTML Parser")
        self.soup=BeautifulSoup(page_content,"html.parser")

    @property
    def info_list(self):
        logger.debug(f"Finding all books in the page using `{Locator.LIST_LOCATOR}`")
        locator=Locator.LIST_LOCATOR
        lists=self.soup.select(locator)
        info=[]#u can use list compression also
        for list in lists:
            info.append(ListParser(list))
        return info

    @property
    def page_count(self):
        logger.debug("Finding all number of catalogue pages available")
        locator=Locator.PAGE_NUM_LOCATOR
        pages=self.soup.select_one(locator).string
        logger.info(f"Found number of catalogue pages are {pages}")
        pattern="[A-z]+ [0-9]+ [A-z]+ ([0-9]+)" #Page 1 of 50
        matcher=re.search(pattern,pages)
        logger.debug(f"Extracted number of pages are `{int(matcher.group(1))}.`")
        return int(matcher.group(1))
