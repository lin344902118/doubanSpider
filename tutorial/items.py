# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class TutorialItem(Item):
    # define the fields for your item here like:
    movie_name = Field()
    movie_director = Field()
    movie_writer = Field()
    movie_roles = Field()
    movie_language = Field()
    movie_date = Field()
    movie_long = Field()
    movie_description = Field()


class ZhihuItem(Item):
    search_title = Field()
    search_title_link = Field()
    search_answer = Field()
    search_answer_link = Field()
    search_answer_writer = Field()


class blogItem(Item):
    head_title = Field()
    description = Field()
    url = Field()

