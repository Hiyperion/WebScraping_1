from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader


class Pregunta(Item):#este objeto depende del item que se va a obtener de la web
    id=Field()
    pregunta = Field()
    # descripcion = Field()

class StackOverFLowSpider(Spider):
    name = "SpiderName"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
    }

    start_urls = ['https://stackoverflow.com/questions']
    def parse(self,response):
        sel=Selector(response)
        preguntas = sel.xpath('//div[@id="questions"]//div[@class="question-summary"]')
        i=1
        for pregunta in preguntas:
            item=ItemLoader(Pregunta(),pregunta)
            item.add_xpath('pregunta','.//h3/a/text()')# el . es por que la busqueda es relativa
            # item.add_xpath('descripcion','.//div[@class="excerpt"]/text()')

            item.add_value('id',i)
            i+=1
            yield item.load_item() #yield retorna un generador (solo se puede iterar una vez) https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

#runs with =>   scrapy runspider WS_scrapy.py -o video.csv -t csv

