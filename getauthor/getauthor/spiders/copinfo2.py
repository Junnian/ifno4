# -*- coding: utf-8 -*-
import scrapy
from getauthor.items import GetauthorItem
from scrapy.http import Request
from scrapy.selector import Selector
import time
from random import random

Url = 'https://scholar.google.com'

class Copinfo2Spider(scrapy.Spider):
    name = 'copinfo2'
    allowed_domains = ['scholar.google.com']
    filenmame = 'copurl1.txt'
    start_urls = []
    scrawl_url = set()
    peopleUrl =set()#记录以爬
    with open(filenmame,'r') as f:
    	lists= f.readlines()
    for url in lists:
    	scrawl_url.add(url)

    def start_requests(self):
       while self.scrawl_url.__len__():
            print self.scrawl_url.__len__()
            url = self.scrawl_url.pop()

            yield Request(url=url, callback=self.parse_info)

    def parse_info(self,response):
        sel = Selector(response)
        i = GetauthorItem()
        url = response.url
        c = url.split('user=')
        i['ID'] = c[1].split('&')[0]
        i['authorurl'] = url
        i['Name'] = sel.xpath('//*[@id="gsc_prf_in"]/text()').extract()[0]
        Fields =sel.xpath('//*[contains(@href,"/citations?view_op=search_author")]/text()').extract()
        i['Fields'] = Fields
        Totalref = sel.xpath('//td[@class="gsc_rsb_std"]/text()').extract()
        if Totalref:
            i['Totalref'] = int(Totalref[0])
            i['ref2'] =int(Totalref[1])
        else:
            i['Totalref'] = 0
            i['ref2'] = 0
        h_index = sel.xpath('//a[contains(@title,"h")]/following::*[1]/text()').extract()
        h_index2 = sel.xpath('//a[contains(@title,"h")]/following::*[2]/text()').extract()
        i10_index = sel.xpath('//a[contains(@title,"i10")]/following::*[1]/text()').extract()
        i10_index2 = sel.xpath('//a[contains(@title,"i10")]/following::*[2]/text()').extract()
        if h_index:
            i['h_index'] = int(h_index[0])
        else: 
            i['h_index'] = 0
        if h_index2:
            i['h_index2'] = int(h_index2[0])
        else:
            i['h_index'] = 0
        if i10_index:
            i['i10_index'] = int(i10_index[0])
        else:
            i['h_index'] = 0
        if i10_index2:
            i['i10_index2'] = int(i10_index2[0])
        else:
            i['h_index'] = 0
        Affi = sel.xpath('//*[@id="gsc_prf_i"]//text()').extract()
        i['Affi'] = Affi[1:len(Affi)-len(Fields)-1]
        coauthorurl = 'https://scholar.google.com/citations?view_op=list_colleagues&hl=zh-CN&user='+i['ID']
                      # https://scholar.google.com/citations?view_op=list_colleagues&hl=zh-CN&json=&user=wtMGHCQAAAAJ
        yield Request(url = coauthorurl,meta={'item':i},callback=self.parse_coauthorurl)

        
    def parse_coauthorurl(self,response):
        i = response.meta['item']
        sel = Selector(response)
        name = sel.xpath('//a[contains(@href,"/citations?user")]//text()').extract()
        Coauthorurl = sel.xpath('//a[contains(@href,"/citations?user")]/@href').extract()
        i['Coauthor'] = name[1:len(name)]
        
        yield i
        
        #可以再把这爬到的合著作者写下
        # # 把合著作者的信息写在一个文件夹里。设置这个爬虫运行完之后，自动开始另一个爬虫
        with open("./copurl2.txt", "w+") as f:
            for courl in Coauthorurl:
            	url = Url + courl
                f.write(url + '\n')