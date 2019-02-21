# -*- coding: utf-8 -*-
import scrapy
from Stock.items import StockItem

class GuchengSpider(scrapy.Spider):
    name = 'gucheng'
    start_urls = ['https://hq.gucheng.com/gpdmylb.html'] # 爬虫起始地址

    def parse(self, response):
        urls = response.xpath('//*[@id="stock_index_right"]/div[3]/section/a/@href').getall() # 获得所有股票详细页面的url
        for i, url in enumerate(urls):
            yield scrapy.Request(url, callback=self.parse_item) # 爬取详细页面

    def parse_item(self, response):
        item = StockItem()
        select = response.xpath('//*[@id="hq_wrap"]/div[1]/section[8]')
        tbody = select.xpath('./div/table/tbody')
        item['name'] = select.xpath('./h3/text()').get()
        item['EPS'] = tbody.xpath('./tr[2]/td[3]/div/text()').get()
        item['NOPAT'] = tbody.xpath('./tr[2]/td[6]/div/text()').get()
        return item