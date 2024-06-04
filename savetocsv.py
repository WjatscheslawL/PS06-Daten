import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


def savetocsv():
    driver = webdriver.Chrome()
    url = "https://tomsk.hh.ru/vacancies/programmist"

    driver.get(url)
    time.sleep(3)

    vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--H8LvOiOGPll0jZvYpxIF')
    parsed_data = []
    i=0
    print("Bcero: ", len(vacancies))
    for vacansy in vacancies:
        try:
            title = vacansy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--SYbxrgpHgHedVTkgI_cA').text
            company = vacansy.find_element(By.CSS_SELECTOR, 'span.company-info-text--O32pGCRW0YDmp3BHuNOP').text
            salary = vacansy.find_element(By.CSS_SELECTOR, 'span.compensation-text--cCPBXayRjn5GuLFWhGTJ').text
            link = vacansy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
        except:
            with open("c:/Util/hherr.txt", 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(vacansy.text)
            i +=1
            print(f"{i} - error parsing")
            continue
        parsed_data.append([title, company, salary, link])
    driver.quit()

    with open("c:/Util/hh.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file,delimiter=';')
        writer.writerow(['name', 'company name', 'lohn', 'link'])
        writer.writerows(parsed_data)
