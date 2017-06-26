# -*- coding: utf-8 -*-
import re
import urlparse

from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import FormRequest,Request

from tutorial.items import TutorialItem



class DoubanloginSpider(CrawlSpider):
    name = "doubanlogin"
    allowed_domains = ["douban.com"]
    start_urls = []

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Host': 'www.douban.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    }

    formdata = {
        'form_email': 'xxx',
        'form_password': 'xxx.',
        'source': 'None',
        'redir': 'https://www.douban.com',
        'remember': 'true',
    }

    def start_requests(self):
        return [Request('https://www.douban.com/login', headers=self.headers, meta={"cookiejar": 1}, callback=self.post_login)]

    def post_login(self, response):
        if 'captcha_image' in response.body:
            print 'Copy the link:'
            link = response.xpath('//img[@class="captcha_image"]/@src').extract()[0]
            print link
            captcha_solution = raw_input('captcha-solution:')
            captcha_id = urlparse.parse_qs(urlparse.urlparse(link).query, True)['id']
            self.formdata['captcha-solution'] = captcha_solution
            self.formdata['captcha-id'] = captcha_id
        return [FormRequest.from_response(response,
                                          meta={'cookiejar': response.meta['cookiejar']},
                                          formdata=self.formdata,
                                          callback=self.after_login)]

    def after_login(self, response):
        pass


