import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


def savetocsv():
    driver = webdriver.Chrome()
    url = "https://www.divan.ru/category/divany-i-kresla"

    driver.get(url)
    time.sleep(3)

    vacancies = driver.find_elements(By.CLASS_NAME, 'lsooF')
    parsed_data = []
    i=0
    print("Bcero: ", len(vacancies))
    for vacansy in vacancies:
        try:
            #print(vacansy)
            # print(vacansy.text)
            span_cont = vacansy.find_element(By.CSS_SELECTOR, 'span[itemprop="name"')

            title = span_cont.text
            print(title)
            meta_tag = vacansy.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]')

            # Extrahieren des Wertes des content-Attributs
            price = meta_tag.get_attribute('content')
            print(price)  # Ausgabe: 66990

            #print(cena)
        except:
            with open("c:/Util/divan.txt", 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(vacansy.text)
            i +=1
            print(f"{i} - error parsing")
            continue
        parsed_data.append([title, price])
    driver.quit()

    with open("c:/Util/divan.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file,delimiter=';')
        writer.writerow(['Нзвание', 'цена'])
        writer.writerows(parsed_data)
