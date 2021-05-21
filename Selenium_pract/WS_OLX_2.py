from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Edge('Selenium_pract/msedgedriver.exe')

driver.get('https://www.olx.com.ec/')

sleep(5)
driver.refresh()
sleep(5)
# boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
for i in range(3): # click en cargar más tres veces
    try:
        #espera por el boton
        boton=WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//button[@data-aut-id="btnLoadMore"]'))
        )

        # boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
        boton.click()
        # sleep(random.uniform(8.0, 10.0))
        WebDriverWait(driver,10).until(#espera a que los elementos esten en el DOM
            EC.presence_of_all_elements_located((By.XPATH,'//li[@data-aut-id="itemBox"]//span[@data-aut-id="itemPrice"]'))
        )

    except:
        break
anuncios = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

for anuncio in anuncios:
    precio = anuncio.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
    print(precio)
    # descripcion = auto.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text
    descripcion = anuncio.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text
    print(descripcion)

print("FINAL")