# doubanSpider
这个一个利用Scrapy来爬取豆瓣电影的例子。通过打开test.txt里面的电影拼接url然后爬取数据。使用方法scrapy crawl douban。
要导出数据scrapy crawl douban -o item.json
该例子对反爬虫做了一些防范，禁止cookie，爬取限制，以及使用随机user-agent，随机代理没有加入
It's a simple example using Scrapy to crawl movie information from douban. start crawl:scrapy crawl douban.
本例子参考自
http://www.cnblogs.com/Shirlies/p/4536880.html
对部分内容进行了修改，旧内容很多不能用，加入了反爬虫
