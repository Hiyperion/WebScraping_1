from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.options import Options
from urllib3.packages.six import b

opts = Options()

# opts.add_argument(
#     "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
# )

# driver=webdriver.Edge('Selenium_pract/msedgedriver.exe',edge_options=opts)
driver=webdriver.Edge('Selenium_pract/msedgedriver.exe')

driver.get('https://listado.mercadolibre.com.ec/repuestos-autos-camionetas-bujias')

# Debemos darle click al boton de disclaimer para que no interrumpa nuestras acciones
try: # Encerramos todo en un try catch para que si no aparece el discilamer, no se caiga el codigo
    disclaimer = driver.find_element(By.XPATH, '//button[@id="cookieDisclaimerButton"]')
    disclaimer.click() # lo obtenemos y le damos click
except Exception as e:
    print (e)
    None



while True:
    links_productos = driver.find_elements(By.XPATH,"//div[@class='ui-search-result__wrapper']//a[@class='ui-search-item__group__element ui-search-link']")
    links_de_pagina=[tag_a.get_attribute('href') for tag_a in links_productos]

    for link in links_de_pagina:
        try:
            driver.get(link)
            titulo = driver.find_element_by_xpath('//h1').text
            precio = driver.find_element_by_xpath('//span[@class="price-tag-amount"]').text

            print(titulo)
            print(precio)

            driver.back()
        except:
            driver.back()
            print("error: ", link)

    try:
        boton_sig=driver.find_element_by_xpath("//span[text()='Siguiente']")
        boton_sig.click()
    except:
        break
        print("Error")
