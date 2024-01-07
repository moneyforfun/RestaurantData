from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import csv
country = input('podaj kraj')
city = input('podaj miasto')

#załadowanie strony
url = 'https://www.starbucks.de/store-locator?types=starbucks'
driver = webdriver.Chrome()
driver.get(url);
sleep(8)
#wpisanie szukanego miejsca
inputFormula = driver.find_element('id','address')
inputFormula.send_keys(f'{city}, {country}')
inputFormula.send_keys(Keys.ENTER)
sleep(2)
resultList = driver.find_elements(By.CLASS_NAME, "store-list-item")
resultSize = len(resultList)
iterations = int(resultSize / 2)

results = []  # List of all Starbucks addresses.

for i in range(0, iterations - 1):
    # Click Info Button
    infoBtn = resultList[i].find_element(By.CLASS_NAME, "abstract-button")
    driver.execute_script("arguments[0].click();", infoBtn)
    sleep(1)
    # Get Adress and append to List
    getStoreAddress = driver.find_elements(By.CLASS_NAME, "store-details-address")
    results.append(getStoreAddress[0].get_attribute('innerHTML'))
    # Click exit button
    exitDiv = driver.find_elements(By.CLASS_NAME, "store-finder-store-header")
    exitBtn = exitDiv[0].find_elements(By.CLASS_NAME, "abstract-button")
    exitBtn[0].get_attribute('innerHTML')


driver.close()
print(results)

with open('Restaurants.csv', mode='w', encoding="utf-8", newline='') as outputFile:
    restaurantCSV = csv.writer(outputFile, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
    #restaurantCSV.writerow(['restaurant', 'street', 'zip', 'city', 'country'])
    restaurantName = 'Starbucks'
    country = 'Poland'
    for restaurant in results:
        street = restaurant.split("\n")[0]
        zipCode = restaurant.split("\n")[1][0:5]
        city = restaurant.split("\n")[1][6:]
        restaurantCSV.writerow([restaurantName, street, zipCode, city, country])