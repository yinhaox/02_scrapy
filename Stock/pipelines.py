# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class StockPipeline(object):

    def process_item(self, item, spider):
        self.f.write(
            '{},{},{}\n'.format(
                item['name'][:-4],
                item['EPS'],
                item['NOPAT']
            )
        )
        return item

    def open_spider(self, spider):
        self.f = open('./data.csv', 'w')
        self.f.write('名称,每股利润,净利润\n')

    def close_spider(self, spider):
        self.f.close()

    