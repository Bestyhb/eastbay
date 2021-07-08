# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class eastbayItem(scrapy.Item):
	#标题
	title = scrapy.Field()
	#价格
	price = scrapy.Field()
	#颜色
	color = scrapy.Field()
	#尺码
	size = scrapy.Field()
	#货号
	sku = scrapy.Field()
	#详情
	details = scrapy.Field()
	#大图链接
	img_ursl = scrapy.Field()
