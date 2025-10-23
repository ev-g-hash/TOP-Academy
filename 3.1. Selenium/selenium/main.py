#<h1 class="jumbotron-heading" value="Cat memes">Cat memes</h1>
#body > main > section > div > h1
#document.querySelector("body > main > section > div > h1")
#------------------------------------------------------------------------
#    -webkit-text-size-adjust: 100%;
#     -webkit-tap-highlight-color: transparent;
#     --blue: #007bff;
#     --indigo: #6610f2;
#     --purple: #6f42c1;
#     --pink: #e83e8c;
#     --red: #dc3545;
#     --orange: #fd7e14;
#     --yellow: #ffc107;
#     --green: #28a745;
#     --teal: #20c997;
#     --cyan: #17a2b8;
#     --white: #fff;
#     --gray: #6c757d;
#     --gray-dark: #343a40;
#     --primary: #007bff;
#     --secondary: #6c757d;
#     --success: #28a745;
#     --info: #17a2b8;
#     --warning: #ffc107;
#     --danger: #dc3545;
#     --light: #f8f9fa;
#     --dark: #343a40;
#     --breakpoint-xs: 0;
#     --breakpoint-sm: 576px;
#     --breakpoint-md: 768px;
#     --breakpoint-lg: 992px;
#     --breakpoint-xl: 1200px;
#     --font-family-sans-serif: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol";
#     --font-family-monospace: SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;
#     --jumbotron-padding-y: 3rem;
#     text-align: center!important;
#     box-sizing: border-box;
#     margin-top: 0;
#     margin-bottom: .5rem;
#     font-family: inherit;
#     line-height: 1.2;
#     color: inherit;
#     font-size: 2.5rem;
#     font-weight: 300;
#----------------------------------------------------------------
#/html/body/main/section/div/h1
#/html/body/main/section/div/h1

"""
# части элементов html

id
tag h1 и т.д.
значение атрибута href="\about"
name
class
селекторы .jumbotron-heading {
            font-weight: 300;
            }
"""


"""
Поиск элементов с помощью Selenium

Для поиска элементов на странице в Selenium WebDriver используются несколько стратегий, позволяющих искать по атрибутам элементов, текстам в ссылках, CSS-селекторам и XPath-селекторам. Для поиска Selenium предоставляет метод find_element, который принимает два аргумента - тип локатора и значение локатора. Существуют следующие методы поиска элементов:

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

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")

button = browser.find_element(By.ID, "submit_button").text

print(button)

time.sleep(10)
