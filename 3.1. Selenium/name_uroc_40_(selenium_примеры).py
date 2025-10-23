"""
продолжение
"""
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "https://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     button = browser.find_element(By.ID, "submit_button")
#     button.click()
#
# finally:
#     time.sleep(2)
#     browser.quit()

#------------------------------------------------------заполнение форм

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "https://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     field_any = browser.find_element(By.NAME, "first_name")
#     field_any.send_keys("Евгений")
#     field_any2 = browser.find_element(By.NAME, "last_name")
#     field_any2.send_keys("Пихтулов")
#     field_any2 = browser.find_element(By.NAME, "firstname")
#     field_any2.send_keys("Тольятти")
#     field_any2 = browser.find_element(By.ID, "country")
#     field_any2.send_keys("Россия")
#     button = browser.find_element(By.ID, "submit_button")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()

#----------------------------------

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://suninjuly.github.io/huge_form.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     elements = browser.find_elements(By.TAG_NAME, "input")
#
#     for el in elements:
#         el.send_keys("Россия")
#
#     button = browser.find_element(By.TAG_NAME, "button")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://suninjuly.github.io/find_xpath_form"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     field_any = browser.find_element(By.NAME, "first_name")
#     field_any.send_keys("Евгений")
#     field_any = browser.find_element(By.NAME, "last_name")
#     field_any.send_keys("Пихтулов")
#     field_any = browser.find_element(By.NAME, "firstname")
#     field_any.send_keys("Тольятти")
#     field_any = browser.find_element(By.ID, "country")
#     field_any.send_keys("Россия")
#
#     button = browser.find_element(By.XPATH, "/html/body/div/form/div[6]/button[3]")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()

"""
# 1) Заходите на сайт
# 2) Вводите в поиск какой-то товар
# 3) Добавляете его в корзину
# 4) Повторить пункт 3
# 5) ищете все добавленные товары
# 6) проверяете кол-во товаров в корзине

"""
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
#
# print("\nпервый товар")
# browser.get("https://www.labirint.ru/")
# product1 = browser.find_element(By.ID, "search-field")
# book1 = "Остров Сокровищ: Роберт Стивенсон"
# product1.send_keys(book1)
#
# product1_button = browser.find_element(By.CSS_SELECTOR, "#searchform > div.b-search-e-input-wrapper > button > span.b-header-b-search-e-srch-icon.b-header-e-sprite-background")
# product1_button.click()
#
# product1_button = browser.find_element(By.CSS_SELECTOR, "#rubric-tab > div.b-search-page-content > section > div > div:nth-child(1) > div.product-card__top > a.product-card__img")
# product1_button.click()
#
# product1_button = browser.find_element(By.XPATH, "/html/body/div[1]/main/article/div[5]/section[4]/div/div[3]/div[2]/button/div/span")
# product1_button.click()
#
# browser.get("https://www.labirint.ru/cart/")
# time.sleep(3)
# print(f"{book1} - добавлена в корзину")
#
#
# print("\nвторой товар")
# product2_button = browser.find_element(By.CSS_SELECTOR, "#minwidth > div.top-header > div > div.b-header > div.b-header__top-part.js-header-top-part > div.b-header-b-logo.col-xs-6.col-sm-6.col-md-2 > div > a > span")
# product2_button.click()
#
# product2 = browser.find_element(By.ID, "search-field")
# book2 = "первая сказка. слушай и играй. колобок"
# product2.send_keys(book2)
#
# product1_button = browser.find_element(By.CSS_SELECTOR, "#searchform > div.b-search-e-input-wrapper > button > span.b-header-b-search-e-srch-icon.b-header-e-sprite-background")
# product1_button.click()
#
# product1_button = browser.find_element(By.CSS_SELECTOR, "#rubric-tab > div.b-search-page-content > section > div > div:nth-child(1) > div.product-card__top > a.product-card__img > img")
# product1_button.click()
#
# product1_button = browser.find_element(By.XPATH, "/html/body/div[1]/main/article/div[5]/section[4]/div/div[3]/div[2]/button/div/span")
# product1_button.click()
#
# browser.get("https://www.labirint.ru/cart/")
# time.sleep(3)
# print(f"{book2} - добавлена в корзину")
#
# browser.quit()





