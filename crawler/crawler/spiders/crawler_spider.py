from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem

# CMD: 
# scrapy crawl crawler -o comments.json

class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains = ["www.thegioididong.com"]
    start_urls = [
        "https://www.thegioididong.com/dtdd-apple-iphone",
    ]

    types = [
       "samsung",
       "oppo",
       "xiaomi",
       "vivo",
       "huawei",
       "mobell",
       "itel",
       "apple-iphone",
       "coolpad",
       "blackberry",
       "realme"
    ]
    for type in types:
        start_urls.append(
            "https://www.thegioididong.com/dtdd-{}".format(type)
        )
        


    def parse(self, response):
       
        telephones = Selector(response).xpath('//body/section/ul/li')

        for telephone in telephones:
           
            item = CrawlerItem()
            item['name'] = telephone.xpath(
                'a/h3/text()').extract_first()
            item['price'] = telephone.xpath(
                'a/div[@class="price"]/strong/text()'
            ).extract_first()
            item['img'] = telephone.xpath(
                'a/img/@data-original'
            ).extract_first()
            if item['img'] is None or len(item['img']) < 1:
                item['img'] = telephone.xpath(
                'a/img/@src'
                ).extract_first()
            
            for row in telephone.xpath('a/figure/span/text()'):
                
                key = row.extract().split(":")[0]
                value = row.extract().split(":")[1]
                key = 'screen' if key.lower() == "màn hình" else key.lower()

                if key.lower() == "ram":
                    ram_data = row.extract().split(",")
                    for data in ram_data:
                        k = data.split(":")[0]
                        v = data.split(":")[1]
                        k = k.strip().lower()
                        # print(k)
                        item[k] = v
                else:
                    item[key] = value
                    print(key, value)
                item["screen"] = item["screen"].replace('\"','"' )
            yield item
          
