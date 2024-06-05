import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


def savetocsv():
    driver = webdriver.Chrome()
    # url = "https://www.pinterest.de/news_hub/5367679720500551217"
    url = "https://www.pinterest.de/pin/123215739801329584/"
    # url = "https://www.emirates.com/de/english/book/featured-fares/"

    driver.get(url)
    time.sleep(3)

    # vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--H8LvOiOGPll0jZvYpxIF')
    # vacancies = driver.find_elements(By.CLASS_NAME, "Jea")
    # vacancies = driver.find_elements(By.CLASS_NAME, "Jea XiG jzS sLG zI7 iyn Hsu")

    # parsdatas = driver.find_elements(By.CLASS_NAME, "Yl- MIw Hb7")
    #parsdatas = driver.find_elements(By.CLASS_NAME,"XiG.sLG.zI7.iyn.Hsu")
    # parsdatas = driver.find_elements(By.CLASS_NAME, "XiG")
    #parsdatas = driver.find_elements(By.CLASS_NAME,"Pj7 sLG XiG eEj m1e")
    #parsdatas = driver.find_elements(By.CLASS_NAME, "Pj7")
    #parsdatas = driver.find_elements(By.CLASS_NAME,"KS5.hs0.un8.C9i.TB_")
    #parsdatas = driver.find_elements(By.CLASS_NAME, "hCL kVc L4E MIw")
    parsdatas = driver.find_elements(By.CLASS_NAME, "Yl-")
    parsed_data = []
    i = 0
    print("Bcero: ", len(parsdatas))
    for item in parsdatas:
        try:
            #title = item.text
            title = item
            print(title)
            # title = item.find_element(By.CLASS_NAME, 'feature-fare__destination').text
            company = '' #item.find_element(By.CLASS_NAME, 'feature-fare-cabin-tabs__cabin_title').text
            salary = '' #item.find_element(By.CLASS_NAME, 'feature-fare-cabin-tabs__price-text').text
            #pichref  = item.find_element(By.CLASS_NAME, 'hCL.kVc.L4E.MIw').get_attribute('src')
            pichref = item.find_element(By.CLASS_NAME, 'hCL').get_attribute('src')
            # link = vacansy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
            link = '' #item.find_element(By.CSS_SELECTOR, 'a.link.feature-fare__action-button.call-to-action.call-to-action__secondary').get_attribute('href')
            # link = vacansy.find_element(By.CLASS_NAME, 'link feature-fare__action-button').text #.get_attribute('href')
        except (ValueError, TypeError):
            with open("c:/Util/programming/parser/error_print.txt", 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(item.text)
            i += 1
            print(f"{i} - error parsing {item.text}")
            continue
        parsed_data.append([title, company, salary, pichref, link])
    driver.quit()

    with open("c:/Util/programming/parser/printer.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['destination', 'cabin_title', 'price', 'image', 'link'])
        writer.writerows(parsed_data)
