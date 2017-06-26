# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from tutorial.items import blogItem


add = 0
class CnblogsSpider(CrawlSpider):
    name = "cnblogs"
    allowed_domains = ["cnblogs.com"]
    start_urls = [
        'https://www.cnblogs.com/lgh344902118',
    ]

    rules = [
        Rule(LinkExtractor(allow=('page=\d+', ), ), callback='parse_item', follow=True),
    ]

    def parse_start_url(self, response):
        return self.parse_item(response)

    def parse_item(self, response):
        global add

        print add

        sel = Selector(response)
        items = []

        titles = sel.xpath('//*[@id="mainContent"]//*[@class="postTitle"]/a/text()').extract()
        descriptions = sel.xpath('//*[@id="mainContent"]//*[@class="postCon"]/div/text()').extract()
        urls = sel.xpath('//*[@id="mainContent"]//*[@class="postTitle"]/a/@href').extract()
        for i in range(len(titles)):
            item = blogItem()
            item['head_title'] = titles[i]
            item['description'] = descriptions[i]
            item['url'] = urls[i]
            items.append(item)
            add += 1
        return items