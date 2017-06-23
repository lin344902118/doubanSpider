# doubanSpider
这个一个利用Scrapy来爬取豆瓣电影的例子。通过打开test.txt里面的电影拼接url然后爬取数据。使用方法scrapy crawl douban。
要导出数据scrapy crawl douban -o item.json
# zhihuSpider
这个是一个打开zhuhu.txt中的问题，在知乎上搜索答案，记录问题，回答者以及连接。使用方法scrapy crawl zhihuSpider
# cnblogs
这是一个爬取某个(我自己的)博客园上的所有文章，保存文章的标题，大致描述以及链接。使用方法scrapy crawl cnblogs
要爬取特定博客园文章，请修改start_url
#该例子对反爬虫做了一些防范，禁止cookie，爬取限制，以及使用随机user-agent，随机代理没有加入
It's a simple example using Scrapy to crawl movie information from douban. start crawl:scrapy crawl douban.
# 本例子参考自
http://www.cnblogs.com/Shirlies/p/4536880.html
对部分内容进行了修改，旧内容很多不能用，加入了反爬虫
# 备注：
douban,zhihu都是使用的BaseSpider，爬取的链接是自己编造的
cnblogs使用的CrawlSpider，爬取首个链接之后匹配的链接，貌似自动去重，不会爬取同个链接两次
如果要保存数据，请在上面的命令后面加上 -o xxx.csv即-o 名称.格式
中文编码没做处理有需要的请自己加上，保存成csv用sublimetext打开正常，json的格式保存的貌似是unicode
例子
scrapy crawl douban -o douban.json
scrapy crawl douban -o douban.csv
# 注意事项:
永远记住不要给服务器造成压力
