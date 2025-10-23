import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

print("\nпервый товар")
browser.get("https://www.labirint.ru/")
product1 = browser.find_element(By.ID, "search-field")
book1 = "Остров Сокровищ: Роберт Стивенсон"
product1.send_keys(book1)

product1_button = browser.find_element(By.CSS_SELECTOR, "#searchform > div.b-search-e-input-wrapper > button > span.b-header-b-search-e-srch-icon.b-header-e-sprite-background")
product1_button.click()

product1_button = browser.find_element(By.CSS_SELECTOR, "#rubric-tab > div.b-search-page-content > section > div > div:nth-child(1) > div.product-card__top > a.product-card__img")
product1_button.click()

product1_button = browser.find_element(By.XPATH, "/html/body/div[1]/main/article/div[5]/section[4]/div/div[3]/div[2]/button/div/span")
product1_button.click()

browser.get("https://www.labirint.ru/cart/")
time.sleep(3)
print(f"{book1} - добавлена в корзину")


print("\nвторой товар")
product2_button = browser.find_element(By.CSS_SELECTOR, "#minwidth > div.top-header > div > div.b-header > div.b-header__top-part.js-header-top-part > div.b-header-b-logo.col-xs-6.col-sm-6.col-md-2 > div > a > span")
product2_button.click()

product2 = browser.find_element(By.ID, "search-field")
book2 = "первая сказка. слушай и играй. колобок"
product2.send_keys(book2)

product1_button = browser.find_element(By.CSS_SELECTOR, "#searchform > div.b-search-e-input-wrapper > button > span.b-header-b-search-e-srch-icon.b-header-e-sprite-background")
product1_button.click()

product1_button = browser.find_element(By.CSS_SELECTOR, "#rubric-tab > div.b-search-page-content > section > div > div:nth-child(1) > div.product-card__top > a.product-card__img > img")
product1_button.click()

product1_button = browser.find_element(By.XPATH, "/html/body/div[1]/main/article/div[5]/section[4]/div/div[3]/div[2]/button/div/span")
product1_button.click()

browser.get("https://www.labirint.ru/cart/")
time.sleep(10)
print(f"{book2} - добавлена в корзину")

browser.quit()
