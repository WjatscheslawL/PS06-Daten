import requests
from bs4 import BeautifulSoup as bs

url = "https://"

response = requests.get(url)
soup = bs(response.text, "html.parser")

rows = soup.find_all("tr")
data = []
for row in rows:
    cols = row.find_all("tr")
    cleaned_cols =[col.text.trip() for col in cols]
    data.append(cleaned_cols)
print(data)


def umvsndeln():
    data = [
        ['100', '200', '300'],
        ['400', '500', '600']
    ]

    numbers = []
    for row in data:
        for text in row:
            number = int(text)
            numbers.append(number)
    print(numbers)

def datafilter():
    data = [
        [100, 200, 300],
        [400, 500, 600],
        [150, 130, 140]
    ]
    list =[]
    for item in  rows:
        if item > 190:
            list.append(item)