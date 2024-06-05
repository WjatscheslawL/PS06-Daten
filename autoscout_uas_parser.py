import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


def savetocsv():
    driver = webdriver.Chrome()
    # url = "https://www.pinterest.de/news_hub/5367679720500551217"
    # url = "https://www.pinterest.de/pin/123215739801329584/"
    # url = "https://www.autoscout24.de/lst/uaz?atype=C&cy=D&desc=0&ocs_listing=include&sort=standard&source=homepage_search-mask&ustate=N%2CU"
    url="https://www.autoscout24.de/lst/uaz/469?atype=C&cy=D&damaged_listing=exclude&desc=0&ocs_listing=include&powertype=kw&search_id=8k2rek87k&sort=standard&source=homepage_search-mask&ustate=N%2CU"

    driver.get(url)
    time.sleep(3)

    # vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--H8LvOiOGPll0jZvYpxIF')
    # vacancies = driver.find_elements(By.CLASS_NAME, "Jea")
    # vacancies = driver.find_elements(By.CLASS_NAME, "Jea XiG jzS sLG zI7 iyn Hsu")

#    parsdatas = driver.find_elements(By.CLASS_NAME, "cldt-summary-full-item")
    parsdatas = driver.find_elements(By.CLASS_NAME,"ListItem_wrapper__TxHWu")
    parsed_data = []
    i = 0
    print("Bcero: ", len(parsdatas))
    for item in parsdatas:
        try:
            # title =
            print(item.text)
            title = item.find_element(By.CLASS_NAME, 'ListItem_title__ndA4s').text
            company = item.find_element(By.CLASS_NAME, 'ListItem_version__5EWfi').text
            salary = item.find_element(By.CLASS_NAME, 'Price_price__APlgs').text
            pichref = '' #item.find_element(By.CLASS_NAME, 'NewGallery_img__cXZQC') # .get_attribute('src')
            vehicledetail = item.find_element(By.CLASS_NAME, 'VehicleDetailTable_container__XhfV1').text
            # link = vacansy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
            link = '' #item.find_element(By.CSS_SELECTOR, 'a.link.feature-fare__action-button.call-to-action.call-to-action__secondary').get_attribute('href')
            # link = vacansy.find_element(By.CLASS_NAME, 'link feature-fare__action-button').text #.get_attribute('href')
        except (ValueError, TypeError):
            with open("c:/Util/programming/parser/error_autoscout.txt", 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(item)
            i += 1
            print(f"{i} - error parsing {item.text}")
            continue
        parsed_data.append([title, company, salary, vehicledetail, pichref, link])
    driver.quit()

    with open("c:/Util/programming/parser/UAZ469.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Name', 'Version', 'price', 'VehicleDetail', 'image', 'link'])
        writer.writerows(parsed_data)
