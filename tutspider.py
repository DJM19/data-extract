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
    sel = Selector(response)
    sites = sel.xpath('.//div[@class="l-tile__item"]')


    for site in sel.xpath('.//div[@class="l-tile__item"]'):
      item = TutsplusItem()
      item["title"] = site.xpath('.//a[@class="c-brick-hotel-booking__link"]/h4/text()').extract()
      items.append(item)
      yield item



