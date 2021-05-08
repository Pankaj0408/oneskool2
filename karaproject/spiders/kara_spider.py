import scrapy

class karaspider(scrapy.spider):
    name = 'kara'
    start_url = [
        "https://www.hindustantimes.com/"
    ]
    def prase(self, response):

        pass