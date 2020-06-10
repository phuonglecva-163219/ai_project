# from scrapy import Spider
# from scrapy.selector import Selector
# from crawler.items import CrawlerItem, DetailItem
# import json
# # CMD: 
# # scrapy crawl crawler -o comments.json

# class CrawlerSpider(Spider):
#     name = "details"
#     allowed_domains = ["www.thegioididong.com"]
#     base_url = "https://www.thegioididong.com/"
#     start_urls = [
#         "https://www.thegioididong.com/dtdd-apple-iphone",
#     ]
    
    
#     def parse(self, response):
#         telephones = Selector(response).xpath('//ul[@class="homeproduct filter-cate"]/li')

#         for telephone in telephones:
#             item = DetailItem()
#             # item['Name'] = telephone.xpath(
#             #     'a/strong/span/text()').extract_first()
#             # item['Info'] = telephone.xpath(
#             #     'a/@href'
#             # ).extract_first()
#             item["name"] = telephone.xpath(
#                 'a/h3/text()'
#             ).extract_first()
#             # infors = telephone.xpath(
#             #     'a/figure/span'
#             # )
#             # for info in infors:
#             #     key = infor.xpath('/text()').extract_first().split(":")[0]
#             #     value = infor.xpath('/text()').extract_first().split(":")[1]
            
#             yield item
