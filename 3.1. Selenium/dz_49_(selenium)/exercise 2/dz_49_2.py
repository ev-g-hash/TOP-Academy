import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://journal.top-academy.ru/ru/auth/login/index")
time.sleep(3)

books_login = browser.find_element(By.ID, "username")
login = "Pihtu_li76"
books_login.send_keys(login)
time.sleep(2)

books_pass = browser.find_element(By.ID, "password")
password = "f5zd559h"
books_pass.send_keys(password)
time.sleep(2)

button = browser.find_element(By.XPATH, "/html/body/mystat/ng-component/ng-component/section/div/div/div/div/div[1]/tabset/div/tab[1]/form/button")
button.click()
time.sleep(5)

button = browser.find_element(By.XPATH, "/html/body/modal-container/div/div/div/button[2]")
button.click()
time.sleep(5)

button = browser.find_element(By.XPATH, "/html/body/mystat/ng-component/ng-component/div/div[3]/div[1]/top-pane/nav/div[2]/a[2]/div")
button.click()
time.sleep(10)
print("Это я изначально в другую группу записывался потом перешёл в Python, а старый кабинет до сих пор висит")








