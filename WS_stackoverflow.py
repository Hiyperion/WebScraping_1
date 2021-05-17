import requests
from bs4 import BeautifulSoup

# USER AGENT PARA PROTEGERNOS DE BANEOS
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}

url = 'https://stackoverflow.com/questions'

resp=requests.get(url,headers=headers)

soup = BeautifulSoup(resp.text,'lxml')#parser

contenedorPreguntas=soup.find(id="questions")
listaPreguntas=contenedorPreguntas.find_all("div",class_="question-summary")
# for pregunta in listaPreguntas:
#     texto_p=pregunta.find("h3").text #hace texto todo dentro del h3
#     descrip_p=pregunta.find(class_='excerpt').text
#     descrip_p=descrip_p.replace('\n','').replace('\r','').strip()#strip elimina espacio al inicio o final del string
#     print(texto_p)
#     print(descrip_p)
#     print("\n")

for pregunta in listaPreguntas:#En caso de que no exista class excerpt
    elemento_textop=pregunta.find("h3")
    texto_p=pregunta.find("h3").text #hace texto todo dentro del h3
    
    descrip_p=elemento_textop.find_next_sibling('div').text#_ apartir de un elemento ir al siguiente primo

    # descrip_p=pregunta.find(class_='excerpt').text
    descrip_p=descrip_p.replace('\n','').replace('\r','').strip()#strip elimina espacio al inicio o final del string
    print(texto_p)
    print(descrip_p)
    print("\n")





