import re
import logging
from locators.listContentLocator import ListContentLocator
from bs4 import BeautifulSoup
"""
This parser contains a class to parse a list
"""

logger=logging.getLogger("scraping.listParser")


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
        logger.debug(f"New book parser  created from `{parent}`.")
        self.parent=parent

    def __repr__(self):
        return f"<{self.name}, {self.rating} star worth \u00A3{self.price}. Here's the link:- {self.link}"

    @property
    def name(self):
        logger.debug("Finding book name....")
        locator=ListContentLocator.NAME_LOCATOR
        item_name=self.parent.select_one(locator).attrs["title"]
        logger.debug(f"Found book name `{item_name}`")
        return item_name

    @property
    def link(self):
        logger.debug("Finding book link....")
        locator=ListContentLocator.LINK_LOCATOR
        item_link=self.parent.select_one(locator).attrs["href"]
        logger.debug(f"Found book link `{item_link}`")
        return item_link

    @property
    def price(self):
        logger.debug("Finding book price....")
        locator=ListContentLocator.PRICE_LOCATOR
        item_price_string=self.parent.select_one(locator).string
        pattern="\u00A3([0-9]+\.[0-9]+)"
        matcher=re.search(pattern,item_price_string)
        logger.debug(f"Found book price `{float(matcher.group(1))}`")
        return float(matcher.group(1))

    @property
    def rating(self):
        logger.debug("Finding book rating....")
        locator=ListContentLocator.RATING_LOCATOR
        item_para_tag=self.parent.select_one(locator).attrs["class"]
        item_rating=[class_name for class_name in item_para_tag if class_name!="star-rating"]
        rating_number=ListParser.RATING.get(item_rating[0]) #None if not found
        logger.debug(f"Found book rating `{rating_number}`")
        return rating_number
