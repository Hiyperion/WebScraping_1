'''Created on lunes, 3 de mayo de 2021
@author: Fabricio Cordova

https://github.com/Hiyperion

Descripcion:
    HTML caracteristicas
    <body> padre de todos
    <p>==parrafos, largos textos
    <a>=links
    <button>= botones acciones
    <form>= formilarios
    <input>= cajas de texto, hijo de form usualmente
    <div>=contenedor, de cualquier cosa
        <div atributo=valor ></div>
    <span>=textos cortos de no mas de una linea
    <h1>Titulos
    <h2>Subtitulos
    <h3> subtitulos de subtitulos
    <h4>
    <h5>
    <img> imagenes
    <li> listas de bullet points
    <table> tablas</table>
    '''
'''
Arquitectura cliente-servidor

cliente envia url a servidor

https://www.google.com /search ?q=WEB+SCRAPING&sourceid=chrome$ie=UTF-8
protocolo   dominio   endpoint  parametros (q=WEB+SCRAPING) & separa los parametros 

endpoint=Identifica que accion va a realizar el servidor
parametros despues de ?
'''

#*Web scraping estatico de una sola pagina  NIVEL 1
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
