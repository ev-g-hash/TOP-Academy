"""
Поиск элементов с помощью Selenium

Для поиска элементов на странице в Selenium WebDriver используются несколько стратегий,
позволяющих искать по атрибутам элементов, текстам в ссылках,
CSS-селекторам и XPath-селекторам. Для поиска Selenium предоставляет метод find_element,
который принимает два аргумента - тип локатора и значение локатора.
Существуют следующие методы поиска элементов:

find_element(By.ID, value) — поиск по уникальному атрибуту id элемента. Если ваши разработчики проставляют всем элементам в приложении уникальный id, то вам повезло, и вы чаще всего будет использовать этот метод, так как он наиболее стабильный;
find_element(By.CSS_SELECTOR, value) — поиск элемента с помощью правил на основе CSS. Это универсальный метод поиска, так как большинство веб-приложений использует CSS для вёрстки и задания оформления страницам. Если find_element_by_id вам не подходит из-за отсутствия id у элементов, то скорее всего вы будете использовать именно этот метод в ваших тестах;
find_element(By.XPATH, value) — поиск с помощью языка запросов XPath, позволяет выполнять очень гибкий поиск элементов;
find_element(By.NAME, value) — поиск по атрибуту name элемента;
find_element(By.TAG_NAME, value) — поиск элемента по названию тега элемента;
find_element(By.CLASS_NAME, value) — поиск по значению атрибута class;
find_element(By.LINK_TEXT, value) — поиск ссылки на странице по полному совпадению;
find_element(By.PARTIAL_LINK_TEXT, value) — поиск ссылки на странице, если текст селектора совпадает с любой частью текста ссылки.
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("-----------------------------------------------------пробные забеги")
browser = webdriver.Chrome()
time.sleep(5)
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
time.sleep(5)

p = browser.find_element(By.TAG_NAME, "p").text
div = browser.find_element(By.TAG_NAME, "div").text
browser.quit()

print(f"--------------------------------------------------это p: ")
print(p)
print()
print(f"--------------------------------------------------это div: ")
print(div)


print(f"\n---------------------------------------------------ввод данных")
driver = webdriver.Chrome()

time.sleep(5)
driver.get("https://suninjuly.github.io/text_input_task.html")
time.sleep(5)

textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")
textarea.send_keys("привет от Евгения!!!!!!!!!!")
time.sleep(5)

submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

submit_button.click()
time.sleep(5)
driver.quit()
print(f"\n---------------------------------------конец программы - ввод данных")


print("-----------------------------------------------------------------парсинг вики")

browser = webdriver.Chrome()

time.sleep(2)
browser.get("https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F")
time.sleep(2)

name = browser.find_element(By.ID, "firstHeading").text
content = browser.find_element(By.ID, "mw-content-text").text
print(name)
print()
print(content)


print("--------------------------------------------------------конец парсинга вики")












