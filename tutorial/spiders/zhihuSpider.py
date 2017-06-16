# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
from tutorial.items import ZhihuItem


class ZhihuSpider(Spider):
    name = "zhihuSpider"
    allowed_domains = ['zhihu.com']
    start_urls = []

    def start_requests(self):
        url_head = 'https://www.zhihu.com/search?type=content&q='
        with open('zhihu.txt', 'r') as f:
            datas = f.readlines()
        for data in datas:
            url = url_head+data
            print url
            self.start_urls.append(url)

        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        response = response.replace(body=response.body.replace('<em>', ''))
        hxs = Selector(response)

        contents = hxs.xpath('//*[@class="zu-main-content"]//*[contains(@class, "list")]')
        item = ZhihuItem()
        for content in contents:
            item['search_title'] = content.xpath('//*[@class="title"]/a/text()').extract()
            item['search_title_link'] = content.xpath('//*[@class="title"]/a/@href').extract()
            item['search_answer'] = content.xpath('//*[@class="content"]//*[contains(@class, "entry-content")]//*[contains(@class, "summary")]/text()').extract()
            item['search_answer_link'] = content.xpath('//*[@class="content"]//*[contains(@class, "entry-content")]//*[contains(@class, "summary")]/a/@href').extract()
            item['search_answer_writer'] = content.xpath('//*[@class="content"]//*[contains(@class, "entry-meta")]//a[contains(@class, "author")]/text()').extract()
            print item
            yield item





