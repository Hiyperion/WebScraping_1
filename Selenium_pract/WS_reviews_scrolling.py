import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.options import Options
# from msedge.selenium_tools import EdgeOptions
# opts = Options()
# opts.capabilities("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")
# opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")

# driver=webdriver.Edge('Selenium_pract/msedgedriver.exe',edge_options=opts)
driver=webdriver.Edge('Selenium_pract/msedgedriver.exe')

# driver.get('https://listado.mercadolibre.com.ec/repuestos-autos-camionetas-bujias')

driver.get('https://www.google.com/maps/place/Restaurante+Amazonico/@40.423706,-3.6872655,17z/data=!4m7!3m6!1s0xd422899dc90366b:0xce28a1dc0f39911d!8m2!3d40.423706!4d-3.6850768!9m1!1b1')

scrollingScript = """
    document.getElementsByClassName('section-layout section-scrollbox cYB2Ge-oHo7ed cYB2Ge-ti6hGc')[0].scroll(0, 20000)
"""
scrolls = 0

sleep(random.uniform(5,6))
while (scrolls != 3):
    driver.execute_script(scrollingScript)
    sleep(random.uniform(5,6))
    scrolls += 1


restaurantReviews = driver.find_elements_by_xpath("//div[@class='ODSEW-ShBeI-content']")
for review in restaurantReviews:
    userLink = review.find_element(By.XPATH,".//div[@class='ODSEW-ShBeI-title']")

    try:
        userLink.click()
        driver.switch_to.window(driver.window_handles[1])


        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'section-layout section-scrollbox')]"))
        )
        # scrollingScropt = """
            # document.getElementsByClassName('"section-layout section-scrollbox cYB2Ge-oHo7ed cYB2Ge-ti6hGc"')[0].scroll(0,20000)
        # """

        USER_SCROLLS = 0
    # Similar a la logica utilizada para hacer scrolling de las opiniones de un restaurante
        while (USER_SCROLLS != 3):
            driver.execute_script(scrollingScript)
            sleep(random.uniform(4, 5))
            USER_SCROLLS += 1
        userReviews =  driver.find_elements_by_xpath("//div[@class='ODSEW-ShBeI-RWgCYc']")
        for userReview in userReviews:
            reviewRating = userReview.find_element(By.XPATH,".//span[@class='ODSEW-ShBeI-H1e3jb']").get_attribute("aria-label")
            reviewRatingNumber = float(''.join(filter(str.isdigit or str.isspace,reviewRating)))#&nbsp es un espacio en html
            reviewText = userReview.find_element(By.XPATH,".//span[@class='ODSEW-ShBeI-text']").text
            print(reviewRatingNumber)
            print(reviewText)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        print(e)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])



