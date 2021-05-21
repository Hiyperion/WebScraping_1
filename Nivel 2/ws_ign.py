from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Articulo(Item):#Noticia
    tituloA = Field()
    contenido = Field()
class Review(Item):
    tituloR = Field()
    calificacion = Field()

class Video(Item):
    tituloV = Field()
    fecha_publicacion = Field()


class IGNspider(CrawlSpider):
    name="SpiderIGN"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 30
    }

    allowed_domains = ['latam.ign.com']
    download_delay=1

    # start_urls=['https://latam.ign.com/se/?type=review&q=god%20of%20war&order_by=']
    start_urls=['https://latam.ign.com/se/?model=article&q=god%20of%20war&order_by=']


    rules = (
        #horizontalidad tipo de informacion
        Rule(
            LinkExtractor(
                allow=r'type='
            ),follow=True
        ),
        #Horizontaldiad paginacion
        Rule(
            LinkExtractor(
                allow=r'&page=\d+'
            ),follow=True
        ),
        #Reviews
        Rule(
            LinkExtractor(
                allow=r'/review/'
            ),follow=True,callback='parser_review'
        ),
        #Videos
        Rule(
            LinkExtractor(
                allow=r'/video|trailer/'
            ),follow=True,callback='parser_video'
        ),
        #Articulos/Noticias
        Rule(
            LinkExtractor(
                allow=r'/news/'
            ),follow=True,callback='parser_news'
        ),
        Rule(
            LinkExtractor(
                allow=r'p=\d+'
            ),follow=True
        )

    )

    def parser_review(self,response):
        item=ItemLoader(Review(),response)
        item.add_xpath('tituloR',"//h1[@class='strong']/text()")
        item.add_xpath('calificacion',"//div[@class='review']//span[@class='side-wrapper side-wrapper hexagon-content']/text()")

        yield item.load_item()

    def parser_video(self,response):
        item=ItemLoader(Video(),response)
        item.add_xpath('tituloV',"//h1[@id='id_title']/text()")
        item.add_xpath('fecha_publicacion',"//span[@class='publish-date']/text()")

        yield item.load_item()

    def parser_news(self,response):
        item=ItemLoader(Articulo(),response)
        item.add_xpath('tituloA',"//h1[@id='id_title']/text()")
        item.add_xpath('contenido',"//div[@id='id_text']//*/text()")

        yield item.load_item()


