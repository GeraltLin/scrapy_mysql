#coding: utf-8
"""
@Time : 2017/11/9 
@Author : lin
"""
import scrapy
from movie_top250.items import MovieTop250Item
class movieSpider(scrapy.Spider):
    name = 'douban_movie'
    allowed_domain = ['douban.com']
    start_urls = ['https://movie.douban.com/top250', ]

    def parse(self, response):
        yield scrapy.Request(response.url,callback=self.parse_page)

        for page in response.xpath('//div[@class = "paginator"]/a'):
            link =  response.urljoin(page.xpath('@href').extract()[0])
            yield scrapy.Request(link,callback=self.parse_page)

    def parse_page(self,response):
        for item in response.xpath('//div[@class = "item"]'):
            movie = MovieTop250Item()
            movie['moviename'] = item.xpath('div[2]/div[1]/a/span[1]/text()').extract()[0]
            movie['rating'] = item.xpath('div[2]/div[2]/div[1]/span[2]/text()').extract()[0]
            yield movie