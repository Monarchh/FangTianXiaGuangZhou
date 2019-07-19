# -*- coding: utf-8 -*-
import scrapy
from FangSpider.items import FangspiderItem

class RentAddrSpider(scrapy.Spider):
    name = 'rent_addr'
    allowed_domains = ['fang.com']
    start_urls = ['https://gz.zu.fang.com/']

    def parse(self, response):
        for info_rel in response.xpath('//dd[@class="info rel"]'):
            item = FangspiderItem()
            item['address'] = info_rel.xpath('./p[@class="gray6 mt12"]/a[1]/span[1]/text()').extract_first()
            yield item
        new_links = response.xpath('//div[@class="fanye"]/a[7]/@href').extract()
        if new_links and len(new_links) > 0:
            new_link = new_links[0]
            yield scrapy.Request("https://gz.zu.fang.com/" + new_link, callback = self.parse)

