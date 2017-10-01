
import scrapy


class TutsplusItem(scrapy.Item):
  
  title = scrapy.Field()
  
  description = scrapy.Field()
  
  address = scrapy.Field()
  
  price= scrapy.Field()

