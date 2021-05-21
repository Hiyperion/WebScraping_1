from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Opinion(Item):
    titulo = Field()
    calificacion = Field()
    contenido = Field()
    autor = Field()

class TripAdvisor(CrawlSpider):
    name="spiderTripAdvisor"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 100
    }

    allowed_domains = ['tripadvisor.com']
    download_delay=1

    start_urls = ['https://www.tripadvisor.com/Hotels-g303845-Guayaquil_Guayas_Province-Hotels.html']


    rules = (
        #Paginacion de Hoteles(h)
        Rule(
            # LinkExtractor(allow=r'Hotels-g303845-oa\d+-'),
            LinkExtractor(allow=r'-oa\d+-'),#BUSCA UNICAMENTE EN PARAMETROS HREF, si el link esta en un button se usa mas parametros
            follow=True
        ),
        #Detalle de hoteles(v)
        Rule(
            LinkExtractor(
                allow=r'/Hotel_Review-',
                restrict_xpaths=["//div[@id='taplc_hsx_hotel_list_lite_dusty_hotels_combined_sponsored_0']//a[@data-clicksource='HotelName']"]
                ),
            follow=True
        ),
        #paginacion review (h)
        Rule(
            LinkExtractor(allow=r'-or\d+-'),
            follow=True
        ),
        #Detalle de perfil de usuario(v)
        Rule(
            LinkExtractor(allow=r'/Profile/',
            restrict_xpaths=["//div[@data-test-target='reviews-tab']//a[contains(@class,'ui_header_link ')]"]
            ),
            follow=True,callback='parser_opinion'
        ),

    )
    def optenerCalificacion(self,texto):
        calificacion=texto.split("_")[-1]
        return calificacion[0]

    def parser_opinion(self,response):
        sel=Selector(response)
        opiniones=sel.xpath("//div[@id='content']/div/div")
        # opiniones=sel.xpath("//div[@class='ui_columns']//div[contains(@class,'ui_card section')]")
        # item=ItemLoader(Opinion,response)
        autor=sel.xpath("//h1/span/text()").get()#Para obtener el valor como tal
        for opinion in opiniones:
            item=ItemLoader(Opinion(),opinion)
            item.add_xpath("titulo",".//div[@class='_3IEJ3tAK _2K4zZcBv']/text()")
            # item.add_xpath("calificacion",".//div[contains(@class,'ui_card section')]//a/div/span[contains(@class,'ui_bubble_rating')]/@class",MapCompose(lambda i: i.split('_')[-1]))
            item.add_xpath("calificacion",".//div[contains(@class,'ui_card section')]//a/div/span[contains(@class,'ui_bubble_rating')]/@class",MapCompose(self.optenerCalificacion))
            item.add_xpath("contenido",".//q/text()",MapCompose(lambda i: i.replace('\n',' ').replace('\r',' ')))
            item.add_value("autor", autor)

            yield item.load_item()