# -*- coding: utf-8 -*-
import scrapy

from eastbay.item import eastbayItem


class eastbaySpider(scrapy.Spider):
	name="product"
	allowed_domains = ['eastbay.com']
	start_urls = ['https://www.eastbay.com/category/sale.html?query=sale%3Arelevance%3AstyleDiscountPercent%3ASALE%3Agender%3AMen%27s%3Abrand%3AASICS+Tiger']
	
	def parse(self,response):
		#在一级页面中，选取所有商品详情页面的链接
		product_urllist=response.xpath("//div[@class='product-container']/a[@class='ProductCard-link']/@href").extract()
		#pass
		#遍历，向每个详情页发送请求
		for product_url in product_urllist:
			yield scrapy.Request(url=product_url,callback=self.parse_detail)
		
		#若有其他目录页则继续发送请求
	def parse_detail(self,response):
		#创建item对象
		item=eastbayItem()
		#标题
		item['title']=response.xpath("//div[@class='app']/span[@class='ProductName-primary']/text()")
		#价格