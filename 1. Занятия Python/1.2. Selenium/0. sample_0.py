import time
import math
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select   ## для выпадающего меню

#----------------------------------------------------------проверка на кликабельность
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    link = "#"
    browser = webdriver.Chrome()
    browser.get(link)

    # заполняет текстовое поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#")
    input1.send_keys("Евгений")

    # нажимаем кнопку button, checkbox, radiobutton
    button = browser.find_element(By.CSS_SELECTOR, "#")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим скрытый элемент в значении кода и возвращем его значение(value)
    x_img = browser.find_element(By.ID, "#")
    x_value_img = x_img.get_attribute("#")
    print(x_value_img)

    # находим элемент, содержащий текст и записываем в переменную если надо
    # выполняем вычисления
    welcome_text_elt = browser.find_element(By.ID, "#")
    x = welcome_text_elt.text
    result = str(math.log(abs(12 * math.sin(int(x)))))
    print(result)

    # выбор выпадающего меню
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value("строка")

    # проскроллить страницу
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # загрузка файла для формы
    element = browser.find_element(By.ID, "file")               # кнопка откуда загружаем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    element.send_keys(file_path)

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(4)
    browser.quit()


"""
------------------------------------------------------модальные окна
"""
"""
Модальные окна
"""

alert = browser.switch_to.alert
alert.accept()                          # закрытие аллерта

"""
Чтобы получить текст из alert, используйте свойство text объекта alert:
"""

alert = browser.switch_to.alert
alert_text = alert.text

"""
Другой вариант модального окна, который предлагает пользователю выбор 
согласиться с сообщением или отказаться от него, называется confirm. 
Для переключения на окно confirm используется та же команда, что и в случае с alert:
"""

confirm = browser.switch_to.alert
confirm.accept()

#Для confirm-окон можно использовать следующий метод для отказа:

confirm.dismiss()

"""
Третий вариант модального окна — prompt — имеет дополнительное поле для ввода текста. 
Чтобы ввести текст, используйте метод send_keys():
"""

prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()

"""
--------------------------------------------------------------вкладки
"""
"""
Переход на новую вкладку браузера
"""
new_window = browser.window_handles[1]              #перейти на вкладку
browser.switch_to.window(new_window)                 #команда для исполнения

first_window = browser.window_handles[0]            # запомнить вкладку чтобы вернуться


"""
----------------------------------------------настройка ожиданий
"""
"""
Неявные ожидания. 
Для этого нам нужно будет убрать time.sleep() и добавить одну строчку 
с методом implicitly wait:

"""
browser.implicitly_wait(5)

"""
--------------------------------------------проверка на кликабельность элемента
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get("https://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text

"""
--------------------------------------------------------------------------------------
"""























