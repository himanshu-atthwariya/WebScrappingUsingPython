from bs4 import BeautifulSoup
from parsers.ListParser import ListParser
"""
In this we are finding the various lists from the website page
"""
class LocateLists:
    def __init__(self,page_content):
        soup=BeautifulSoup(page_content,"html.parser")
        locator_lists="div.container-fluid div.page_inner div.row div.col-sm-8.col-md-9 section ol.row li"
        lists=soup.select(locator_lists)
        for list in lists:
            print(ListParser(list))
