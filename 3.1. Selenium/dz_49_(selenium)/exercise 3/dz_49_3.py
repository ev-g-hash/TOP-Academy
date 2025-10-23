import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F")
time.sleep(2)

name = browser.find_element(By.ID, "firstHeading").text
my_list = name.split()

name2 = browser.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[1]/p[3]").text
my_list2 = name2.split()

print("скопировано с сайта 'Википедия'")
print(my_list)
print(my_list2)

filename = "test.csv"

#запись
with open(filename, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow(my_list)
    writer.writerow(my_list2)
    print("записано в файл 'test.csv'")
# чтение
with open(filename, encoding="utf-8") as file:
    reader = csv.reader(file)
    rows = list(reader)
    print("чтение из файла 'test.csv'")
    print(*rows)
















