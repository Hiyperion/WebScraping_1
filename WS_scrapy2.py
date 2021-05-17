from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess
class Noticia(Item):
    titular=Field()
    descripcion=Field()

class ElUniversoSpider(Spider):
    name="MiSpiderDos"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
    }
    start_urls=["https://www.eluniverso.com/deportes"]
    def parse(self,response):
        sel=Selector(response)
        noticias=sel.xpath("//div[contains(@class,'content-feed')]//div[contains(@class,'card-content')]")
        # noticias=sel.xpath("//div[contains(@class,'content-feed')]/ul/li")#obtiene con imagen
        for noticia in noticias:
            item=ItemLoader(Noticia(),noticia)
            item.add_xpath('titular','.//h2/a/text()')
            item.add_xpath('descripcion','.//p/text()')
            yield item.load_item()

    # def parse(self,response):#_usando Beautifulsoup
    #     soup=BeautifulSoup(response.body)
    #     contenedor_noticias=soup.find_all(class_="feed | divide-y relative")
    #     for contenedor in contenedor_noticias:
    #         noticias=contenedor.find_all(class_="relative",recursive=False)
    #         for noticia in noticias:
    #             item=ItemLoader(Noticia(),response.body)
    #             titular=noticia.find("h2").text
    #             descripcion=noticia.find("p")
    #             if descripcion != None:
    #                 descripcion=descripcion.text
    #             else:
    #                 descripcion="N/A"
    #             item.add_value('titular',titular)
    #             item.add_value('descripcion',descripcion)

    #             yield item.load_item()


process=CrawlerProcess({
    'Feed_FORMAT':'csv',
    'FEED_URI': 'resultados.csv'
})

process.crawl(ElUniversoSpider)
process.start()