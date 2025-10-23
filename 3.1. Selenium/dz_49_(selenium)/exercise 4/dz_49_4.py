import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://www.survio.com/ru/"
browser.get(link)
button1 = browser.find_element(By.XPATH, "/html/body/section[3]/div/div[4]/span").text
button2 = browser.find_element(By.XPATH, "/html/body/header/div[1]/div/ul/li[2]/span").text
button3 = browser.find_element(By.XPATH, "/html/body/header/div[1]/div/ul/li[1]/span").text

print(f"на сайте - ( {link} ), имеется кнопка - ( {button1} )")
print(f"на сайте - ( {link} ), имеется кнопка - ( {button2} )")
print(f"на сайте - ( {link} ), имеется кнопка - ( {button3} )")
browser.quit()

print()

browser = webdriver.Chrome()
link = "https://books.yandex.ru/"
browser.get(link)
div = browser.find_element(By.CSS_SELECTOR, "body > div.main-content.MainLayout_content__p_cdm > div > div.LandingPage_container__eN5QU.LandingPage_annual__I_TkK > div.LandingMainWrapper_container__cqTBO.LandingMain_annual__3_IQR.LandingPage_mainSection__Hse7g > div.LandingMain_container__xD_Sw > form > h1").text
button = browser.find_element(By.XPATH, "/html/body/header/div/div[3]/button[1]").text

print(f"на сайте - ( {link} ), имеется блок - ( {div} )")
print(f"на сайте - ( {link} ), имеется кнопка - ( {button} )")
browser.quit()













