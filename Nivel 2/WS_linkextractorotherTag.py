from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader


class ProductoF(Item):
    nombre = Field()
    precio = Field()

class FarmaciaSpider(CrawlSpider):
    name = "farmaciaSpider"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 30
    }
    download_delay=1

    allowed_domains = ["cruzverde.cl"]
 
    start_urls = ["https://www.cruzverde.cl/medicamentos/"]

    rules = (
        Rule(
            LinkExtractor(
                allow=r'start=',
                tags=('a','button'),
                attrs=('href','data-url')

            ),follow=True,callback='parcer_farmacia'
        ),
    )

    def parcer_farmacia(self, response):
        sel=Selector(response)

        productos=sel.xpath('//div[@class="col-12 col-lg-4"]')
        for producto in productos:
            item=ItemLoader(ProductoF(),producto)
            item.add_xpath("nombre",".//div[@class='tile-body px-3 pt-3 pb-0 d-flex flex-column pb-0']//div[@class='pdp-link']/a/text()",MapCompose(lambda i: i.replace('\n','').replace('\r','').strip()))
            item.add_xpath("precio",".//div[@class='price']//span[@class='sales d-flex flex-wrap mb-1 align-items-center']//span[@class='value']/text()",MapCompose(lambda i: i.replace('\n','').replace('\r','').strip()))
            #el precio de algunos items no se obtienen por que esta en otro contenedor

            # item.add_xpath('nombre', './/div[@class="tile-body px-3 pt-3 pb-0 d-flex flex-column pb-0"]//div[@class="pdp-link"]/a/text()')
            # item.add_xpath('precio',
                            # './/span[contains(@class, "value ")]/text()')

            yield item.load_item()