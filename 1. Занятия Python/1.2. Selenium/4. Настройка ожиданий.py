# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# browser.get("https://suninjuly.github.io/wait1.html")
#
# browser.implicitly_wait(5)
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text


"""
Задание: Про Exceptions
Теперь мы знаем, как настроить ожидание поиска элемента.
Во время поиска WebDriver каждые 0.5 секунды проверяет,
появился ли нужный элемент в DOM-модели браузера
(Document Object Model — «объектная модель документа»,
интерфейс для доступа к HTML-содержимому сайта). Если произойдет ошибка,
то WebDriver выбросит одно из следующих исключений (exceptions):

Если элемент не был найден за отведенное время, то мы получим NoSuchElementException.
Если элемент был найден в момент поиска, но при последующем обращении к элементу DOM изменился, то получим StaleElementReferenceException. Например, мы нашли элемент Кнопка и через какое-то время решили выполнить с ним уже известный нам метод click. Если кнопка за это время была скрыта скриптом, то метод применять уже бесполезно — элемент "устарел" (stale) и мы увидим исключение.
Если элемент был найден в момент поиска, но сам элемент невидим
(например, имеет нулевые размеры), и реальный пользователь не смог
бы с ним взаимодействовать, то получим ElementNotVisibleException.
Знание причин появления исключений помогает отлаживать тесты и понимать,
где находится баг в случае его возникновения.

Задание:

Какую ошибку вы увидите в консоли, если попытаетесь выполнить команду
browser.find_element(By.ID, "button") после открытия страницы
https://suninjuly.github.io/cats.html?
"""

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "https://suninjuly.github.io/cats.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
# browser.find_element(By.ID, "button")


"""
Explicit Waits (WebDriverWait и expected_conditions)
В предыдущем шаге мы решили проблему с ожиданием элементов на странице. 
Однако методы find_element проверяют только то, что элемент появился на странице. 
В то же время элемент может иметь дополнительные свойства, которые могут быть 
важны для наших тестов. Рассмотрим пример с кнопкой, которая отправляет данные:

Кнопка может быть неактивной, то есть её нельзя кликнуть;
Кнопка может содержать текст, который меняется в зависимости от действий пользователя. 
Например, текст "Отправить" после нажатия кнопки поменяется на "Отправлено";
Кнопка может быть перекрыта каким-то другим элементом или быть невидимой.

----------------------------------------------------------------------------
Чтобы тест был надежным, нам нужно не только найти кнопку на странице, 
но и дождаться, когда кнопка станет кликабельной. Для реализации подобных 
ожиданий в Selenium WebDriver существует понятие явных ожиданий (Explicit Waits), 
которые позволяют задать специальное ожидание для конкретного элемента. Задание явных 
ожиданий реализуется с помощью инструментов WebDriverWait и expected_conditions. 
Улучшим наш тест:
------------------------------------------------------------
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# browser = webdriver.Chrome()
#
# browser.get("https://suninjuly.github.io/wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text


"""
element_to_be_clickable вернет элемент, когда он станет кликабельным, или вернет 
False в ином случае.

Обратите внимание, что в объекте WebDriverWait используется функция until, 
в которую передается правило ожидания, элемент, а также значение, по которому 
мы будем искать элемент. В модуле expected_conditions есть много других правил, 
которые позволяют реализовать необходимые ожидания:

title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present

Описание каждого правила можно найти на 
https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions.

Если мы захотим проверять, что кнопка становится неактивной после отправки данных, 
то можно задать негативное правило с помощью метода until_not:

# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
button = WebDriverWait(browser, 5).until_not(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
"""

"""
Задание: ждем нужный текст на странице
Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха 
по строго заданной цене. Более высокая цена нас не устраивает, 
а по более низкой цене объект успеет забронировать кто-то другой.

В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу https://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу 
(используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100,
используйте метод text_to_be_present_in_element из библиотеки expected_conditions.

Если все сделано правильно и быстро, то вы увидите окно с числом.
Отправьте его в качестве ответа на это задание.

"""
# import math
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# try:
#     link = "https://suninjuly.github.io/explicit_wait2.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     button = browser.find_element(By.ID, "book")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#
#     button = browser.find_element(By.ID, "book")
#     WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
#     button.click()
#
#     button = browser.find_element(By.ID, "solve")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#
#     welcome_text_elt = browser.find_element(By.ID, "input_value")
#     x = welcome_text_elt.text
#     result = str(math.log(abs(12 * math.sin(int(x)))))
#
#     input1 = browser.find_element(By.ID, "answer")
#     input1.send_keys(result)
#
#     button = browser.find_element(By.ID, "solve")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()



"""
В этом уроке мы постарались собрать ссылки на ресурсы, где вы сможете найти 
дополнительную информацию по использованию Selenium и о тонкостях при работе с ним:

Полезные ссылки

http://chromedriver.chromium.org/getting-started
https://www.guru99.com/selenium-tutorial.html — Туториал на английском, ориентирован на Java.
https://www.guru99.com/live-selenium-project.html — Можно попробовать писать автотесты для демо-сайта банка. Тоже Java.
http://barancev.github.io/good-locators/ — что такое хорошие селекторы
http://barancev.github.io/what-is-path-env-var/ — что за PATH переменная? 
Ожидания в Selenium WebDriver

https://www.selenium.dev/documentation/webdriver/waits/
https://stackoverflow.com/questions/15122864/selenium-wait-until-document-is-ready
https://blog.codeship.com/get-selenium-to-wait-for-page-load/
http://barancev.github.io/slow-loading-pages/
http://barancev.github.io/page-loading-complete/

"""









