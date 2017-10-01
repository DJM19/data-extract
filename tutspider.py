from scrapy.spiders import Spider
from scrapy.selector import Selector
from tutsplus.items import TutsplusItem
from scrapy.http    import Request
import re
 
class MySpider(Spider):
  name = "hotels"
  allowed_domains   = ["hotels.ctrip.com"]
  start_urls = ["http://english.ctrip.com/hotels/taipei-hotels-list-617/#ctm_ref=hod_hp_sb_lst/"]

  def parse(self, response):
    items = []
    items1 = []
    sel = Selector(response)
    
    for site in sel.xpath('.//div[@class="l-tile__item"]'):
      item = TutsplusItem()
      item["title"] = site.xpath('.//a[@class="c-brick-hotel-booking__link"]/h4/text()').extract()
      item["description"] = site.xpath('.//div[@class="c-brick-hotel-booking__desc"]/text()').extract()
      item["address"] = site.xpath('.//div[@class="c-brick-hotel-booking__addr"]/text()').extract()
      item["price"] = site.xpath('.//div[@class="c-brick-hotel-booking__price-box"]//span[@class="o-price__num"]/text()').extract()
      items.append(item)
      yield item
    next_page = response.css('li.next a::attr(href)').extract_first()
    if next_page is not None:
      next_page = response.urljoin(next_page)
      yield scrapy.Request(next_page, callback=self.parse)



