'''Created on miércoles, 5 de mayo de 2021
@author: Fabricio Cordova

https://github.com/Hiyperion

Descripcion:
    Extract data from wikipedia

    '''
#Extraer informacion de idiomas
import requests
from lxml import html
url="https://www.wikipedia.org/"

encabezados = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}
resp=requests.get(url,headers=encabezados)
# print(resp)
parser=html.fromstring(resp.text)

ingles=parser.get_element_by_id("js-link-box-en")
# print(ingles.text_content())

inglesPat=parser.xpath("//a[@id='js-link-box-en']/strong/text()")
# print(inglesPat)

allIdiomas=parser.xpath("//div[contains(@class,'central-featured-lang')]//strong/text()")

# print(allIdiomas)

idiomas=parser.find_class("central-featured-lang")# encuentra  clases y si hay un espacio en la clase del html entonces se dice que tiene dos clases y esta funcion obtiene una

for idioma in idiomas:
    print(idioma.text_content())


















