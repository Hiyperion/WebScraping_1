
#* Web scraping estatico de una sola pagina  NIVEL 1
    """
    Toda la info en una pagina web y la pagina no carga dinamicamente
    Librerias requests, lxml, beautifulsoup, scrapy


    """
#*Web scraping estatico de varias paginas NIVEL 2
    """
    Crolling horizontal (paginacion) y vertical (pagina del detalle del item)
    Del mismo dominio
    Libreria Scrapy

    """

#*Web Scraping dinamico  Nivel 3
    """
    Automatizar acciones de un navegador
    Librerias: Selenium
    """
#*Web scraping de APIS
#*Autenticacion, captchas, extraer info

#_ PASOS DEL WEB SCRAPING

"""
1. Definir URL semilla, pagina principal para la estraccion de datos

2. Realizar un Request a la url semilla

3. Obtener respuesta del request en html

4. A partir de la respuesta Obtener  informacion, extraer datos XPATH

5. Volver al paso 2 con otras urls del mismo dominio

"""

#* XPATH= Lenguaje que permite construir expresiones que recorren y procesan un documento XML, HTML es un XML 

#* prefijo de busqueda o eje de busqueda
""" // en todo el documento
    / en la raiz
    ./ relativa donde me encuentro en el documento
"""

#* step, definir el nodo donde se enfocara la busqueda
#_ nombre del tag donde se va a focalizar la busqueda

#* definir predicados, para focalizar aun mas la busqueda
#* buesqueda por atributos se usa la @ antes del atributo, 
# _ //h1[@id="valor"]

#* busqueda dentro de un hijo
    #_ // padre/hijo
#* Indexacion

#_ //div/li[1]

#_ //div/li[last()]

#_ //div/li[position()=2] #* permite usar funciones

#_ //div/li[contains(@id, "elemento")], entre otros documentacion en links de Documentation folder


#* otras funciones

#_ //div/li[text()] 








