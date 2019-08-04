import re
from locators.listContentLocator import ListContentLocator
from bs4 import BeautifulSoup
"""
This parser contains a class to parse a list
"""
class ListParser:
    """
    This class takes a list as argument and then we parse its various elements
    """
    RATING={
        "One":1,
        "Two":2,
        "Three":3,
        "Four":4,"Five":5
    }

    def __init__(self,parent):#parent takes list
        self.parent=parent

    def __repr__(self):
        return f"<{self.name}, {self.rating} star worth \u00A3{self.price}. Here's the link:- {self.link}"

    @property
    def name(self):
        locator=ListContentLocator.NAME_LOCATOR
        item_name=self.parent.select_one(locator).attrs["title"]
        return item_name

    @property
    def link(self):
        locator=ListContentLocator.LINK_LOCATOR
        item_link=self.parent.select_one(locator).attrs["href"]
        return item_link

    @property
    def price(self):
        locator=ListContentLocator.PRICE_LOCATOR
        item_price_string=self.parent.select_one(locator).string
        pattern="\u00A3([0-9]+\.[0-9]+)"
        matcher=re.search(pattern,item_price_string)
        return float(matcher.group(1))

    @property
    def rating(self):
        locator=ListContentLocator.RATING_LOCATOR
        item_para_tag=self.parent.select_one(locator).attrs["class"]
        item_rating=[class_name for class_name in item_para_tag if class_name!="star-rating"]
        rating_number=ListParser.RATING.get(item_rating[0]) #None if not found
        return rating_number
