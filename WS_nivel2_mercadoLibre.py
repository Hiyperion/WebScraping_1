from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Articulo(Item):
    titulo = Field()
    precio = Field()
    descripcion = Field()

class ArañaMercadLibre(CrawlSpider):
    name = 'mercadoLibre'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT':20
    }

    download_delay = 1

    allowed_domains = ['listado.mercadolibre.com.ec','articulo.mercadolibre.com.ec']#restringir expectro de busqueda

    start_urls = ['https://listado.mercadolibre.com.ec/animales-mascotas/perros/']


    rules = (
        #paginacion
        Rule(
            LinkExtractor(
                allow = r'/_Desde_'
            ),follow=True
        ),
        #Detalle productos
        Rule(
            LinkExtractor(
                allow = r'/MEC-'
                ),follow = True, callback='parse_items'
        ),
    )

    def parse_items(self,response):
        # sel = Selector(response)
        item = ItemLoader(Articulo(),response)#se puede pasar directo el response por que no se hace iteración

        item.add_xpath('titulo',"//h1[contains(@class,'title')]/text()")
        item.add_xpath('descripcion',"//div[contains(@class,'description')]/p/text()",MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip()))#usando funcion anonima
        item.add_xpath('precio',"//div[@class='ui-pdp-price__second-line']/span//span[@class='price-tag-fraction']/text()")

        yield item.load_item()