# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class GetauthorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Name = Field()
    Fields = Field()
    # Paper = Field()
    Affi  = Field()#机构
    # Email = Field()#有的可能有邮箱
    Coauthor = Field()#合著作者
    authorurl =Field() #当前作者主页
    Totalref = Field()#总引用量
    ID = Field()#用来标志作者的唯一性
    ref2 = Field()
    h_index = Field()
    h_index2 =Field()
    i10_index = Field()
    i10_index2 =Field()

    pass
