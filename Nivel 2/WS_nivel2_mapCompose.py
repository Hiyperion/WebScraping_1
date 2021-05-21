from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader


# from scrapy.crawler import CrawlerProcess

class Hotel(Item):
    nombre = Field()
    # score = Field() # El precio ahora carga dinamicamente. Por eso ahora obtenemos el score del hotel
    descripcion = Field()
    amenities = Field()

class TripAdvisor(CrawlSpider):
    name = "hotelestripadvisor"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
    }

    allowed_domains = ['tripadvisor.com']

    # start_urls=["https://www.tripadvisor.es/Hotels-g303845-Guayaquil_Guayas_Province-Hotels.html"]
    start_urls = ['https://www.tripadvisor.com/Hotels-g303845-Guayaquil_Guayas_Province-Hotels.html']

    download_delay=2 #Tiempo entre requerimientos en segundos

    rules = (
        Rule( # Regla de movimiento VERTICAL hacia el detalle de los hoteles
            LinkExtractor(
                allow=r'/Hotel_Review-' # Si la URL contiene este patron, haz un requerimiento a esa URL
            ), follow=True, callback="parse_hotel"), # El callback es el nombre de la funcion que se va a llamar con la respuesta al requerimiento hacia estas URLs
    )
    def modifyText(self,text):
        #Do something with text
        return text.replace('A','B')


    def parse_hotel(self,response):
        sel=Selector(response)
        item= ItemLoader(Hotel(),sel)
        # item.add_xpath('nombre',"//h1[@id='HEADING']/text()")
        # item.add_xpath('nombre',"//h1[@id='HEADING']/text()")
        item.add_xpath('nombre', '//h1[@id="HEADING"]/text()')
        # item.add_xpath('precio',"//div[@class='_36QMXqQj]/text()'") # los numeros randoms en la clase cambian  luego de un tiempo, es necesario otro xpath
        item.add_xpath('precio','xpath',MapCompose(self.modifyText))
        #_ si se coloca //div[1] se optiene el primero de varios
        # item.add_xpath('precio',"//div[@class='_36QMXqQj]/text()'") # el precio requiere de un xpath mas complejo que cubra las variaciones de un url a otro, por ahora //div[@class="premium_offers_area offers"]//div[contains(@class,'ui_columns')]/div/div tiene coincidencias
        item.add_xpath('descripcion',"//div[@id='component_12']//div[contains(@class,'ui_columns')]//div[contains(@class,'ruteS')]/div[1]/div/text()")
        item.add_xpath('amenities',"//div[contains(@data-test-target,'amenity')]/text()")

        yield item.load_item()