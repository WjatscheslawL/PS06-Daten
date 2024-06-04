import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


def savetocsv():
    driver = webdriver.Chrome()
    #url = "https://www.pinterest.de/news_hub/5367679720500551217"
    #url = "https://www.pinterest.de/pin/123215739801329584/"
    url = "https://www.emirates.com/de/english/book/featured-fares/"

    driver.get(url)
    time.sleep(3)

    #vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--H8LvOiOGPll0jZvYpxIF')
    #vacancies = driver.find_elements(By.CLASS_NAME, "Jea")
    #vacancies = driver.find_elements(By.CLASS_NAME, "Jea XiG jzS sLG zI7 iyn Hsu")

    vacancies = driver.find_elements(By.CLASS_NAME, "feature-fare__container")
    parsed_data = []
    i=0
    print("Bcero: ", len(vacancies))
    for vacansy in vacancies:
        try:
            #title = vacansy.text
            title = vacansy.find_element(By.CLASS_NAME, 'feature-fare__destination').text
            company = vacansy.find_element(By.CLASS_NAME, 'feature-fare-cabin-tabs__cabin_title').text
            salary = vacansy.find_element(By.CLASS_NAME, 'feature-fare-cabin-tabs__price-text').text
            pichref = vacansy.find_element(By.CLASS_NAME, 'feature-fare__fare-image').get_attribute('src')
            #link = vacansy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
            link = vacansy.find_element(By.CSS_SELECTOR, 'a.link.feature-fare__action-button.call-to-action.call-to-action__secondary') .get_attribute('href')
            #link = vacansy.find_element(By.CLASS_NAME, 'link feature-fare__action-button').text #.get_attribute('href')
        except:
            with open("c:/Util/hherr.txt", 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(vacansy.text)
            i +=1
            print(f"{i} - error parsing {vacansy.text}" )
            continue
        parsed_data.append([title, company, salary, pichref, link])
    driver.quit()

    with open("c:/Util/emirates_book_featured-fares.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file,delimiter=';')
        writer.writerow(['destination', 'cabin_title', 'price', 'image', 'link'])
        writer.writerows(parsed_data)
