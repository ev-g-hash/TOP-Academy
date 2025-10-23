"""
Работа со списками
На веб-страницах мы также встречаем раскрывающиеся (выпадающие) списки.
У таких списков есть несколько важных особенностей:

У каждого элемента списка обычно есть уникальное значение атрибута value
В списках может быть разрешено выбирать как только один, так и несколько вариантов,
в зависимости от типа списка
Визуально списки могут различаться тем, что в одном случае все варианты скрыты
в выпадающем меню (https://suninjuly.github.io/selects1.html),
а в другом все варианты или их часть видны (https://suninjuly.github.io/selects2.html)
Но для взаимодействия с любым вариантом списка мы будем использовать одни и те же методы
Selenium.

Есть более удобный способ, для которого используется специальный класс
Select из библиотеки WebDriver. Вначале мы должны инициализировать новый объект,
передав в него WebElement с тегом select. Далее можно найти любой вариант из списка
с помощью метода select_by_value(value):

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("1") # ищем элемент с текстом "Python"


Можно использовать еще два метода: select.select_by_visible_text("text")
и select.select_by_index(index). Первый способ ищет элемент по видимому тексту,
например, select.select_by_visible_text("Python") найдёт "Python" для нашего примера.

Второй способ ищет элемент по его индексу или порядковому номеру.
Индексация начинается с нуля. Для того чтобы найти элемент с текстом "Python",
нужно использовать select.select_by_index(1), так как опция с индексом 0 в данном
примере имеет значение по умолчанию равное "--".

"""

"""
Задание: работа с выпадающим списком
Для этой задачи мы придумали еще один вариант капчи для роботов. 
Придется немного переобучить нашего робота, чтобы он справился с новым заданием.

Напишите код, который реализует следующий сценарий:

Открыть страницу https://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
Если все сделано правильно и достаточно быстро 
(в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. 
Отправьте полученное число в качестве ответа для этого задания.

Когда ваш код заработает, попробуйте запустить его на 
странице https://suninjuly.github.io/selects2.html. 
Ваш код и для нее тоже должен пройти успешно.
"""
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
#
# try:
#     link = "https://suninjuly.github.io/selects1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     num1_text_elt = browser.find_element(By.ID, "num1")
#     num_1 = num1_text_elt.text
#
#     num2_text_elt = browser.find_element(By.ID, "num2")
#     num_2 = num2_text_elt.text
#     result = str(int(num_1) + int(num_2))
#
#     select = Select(browser.find_element(By.ID, "dropdown"))
#     select.select_by_value(result)
#
#
#     button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
#
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()

"""
Метод execute_script
Рассмотрим еще один очень полезный и мощный метод, но он требует хотя бы 
минимальных знаний JavaScript. С помощью метода execute_script можно 
выполнить программу, написанную на языке JavaScript, как часть 
сценария автотеста в запущенном браузере. Зачем это может понадобиться, 
если в автотестах мы стараемся взаимодействовать с интерфейсом сайта как 
обычный пользователь, нажимая кнопки, выбирая пункты меню и вводя текст в текстовые поля?

Давайте попробуем вызвать alert в браузере с помощью WebDriver. Пример сценария:

from selenium import webdriver
browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")

"""

# import time
# from selenium import webdriver
# browser = webdriver.Chrome()

# # вызов алерта
# time.sleep(2)
# browser.execute_script("alert('Robots at work');")
# time.sleep(2)

# # изменение заголовка и вызов алерта
# time.sleep(2)
# browser.execute_script("document.title='Script executing';alert('Robots at work');")
# time.sleep(2)

"""
Пример задачи для execute_script
Давайте теперь рассмотрим реальную ситуацию, когда пользователь должен кликнуть 
на элемент, который внезапно оказывается перекрыт другим элементом на странице.

Для клика в WebDriver мы используем метод click(). Если элемент оказывается
перекрыт другим элементом, то наша программа вызовет следующую ошибку:

selenium.common.exceptions.WebDriverException: Message: unknown error: 
Element <button type="submit" class="btn btn-default" style="margin-bottom: 
1000px;">...</button> is not clickable at point (87, 420). 
Other element would receive the click: <p>...</p>

Из описания ошибки можно понять, что указанный нами элемент нельзя кликнуть в данной точке, 
т.к. клик произойдёт на другом элементе с тегом <p>.

Чтобы увидеть пример данной ошибки, запустите следующий скрипт:

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
button.click()
"""

"""
Мы дополнительно передали в метод scrollIntoView аргумент true, 
чтобы элемент после скролла оказался в области видимости. 
Другие возможные параметры метода можно посмотреть здесь: https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView

В итоге, чтобы кликнуть на перекрытую кнопку, нам нужно выполнить следующие команды в коде:
-------------------------------------------------------------------------------------------
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
--------------------------------------------------------------------------------------------
"""
"""
Также можно проскроллить всю страницу целиком на строго заданное количество пикселей. 
Эта команда проскроллит страницу на 100 пикселей вниз:

browser.execute_script("window.scrollBy(0, 100);")
!Важно. Мы не будем в этом курсе изучать, как работает JavaScript, 
и обойдемся только приведенным выше примером скрипта с прокруткой страницы. 
Для сравнения приведем скрипт на этом языке, который делает то же, 
что приведенный выше пример для WebDriver:

// javascript
button = document.getElementsByTagName("button")[0];
button.scrollIntoView(true);

"""

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# time.sleep(4)
# button = browser.find_element(By.TAG_NAME, "button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()
# time.sleep(4)


"""
Задание на execute_script
В данной задаче вам нужно будет снова преодолеть капчу для роботов и
справиться с ужасным и огромным футером, который дизайнер всё никак не успевает 
переделать. Вам потребуется написать код, чтобы:

+Открыть страницу https://SunInJuly.github.io/execute_script.html.
+Считать значение для переменной x.
+Посчитать математическую функцию от x.
+Проскроллить страницу вниз.
+Ввести ответ в текстовое поле.
+Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".

Если все сделано правильно и достаточно быстро 
(в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. 
Отправьте полученное число в качестве ответа для этого задания.

Для этой задачи вам понадобится использовать метод execute_script, 
чтобы сделать прокрутку в область видимости элементов, перекрытых футером.

"""
# import math
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
#
# try:
#     link = "https://SunInJuly.github.io/execute_script.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     text_elt = browser.find_element(By.ID, "input_value")
#     x = text_elt.text
#     result = str(math.log(abs(12 * math.sin(int(x)))))
#
#     input1 = browser.find_element(By.ID, "answer")
#     input1.send_keys(result)
#
#     checkbox = browser.find_element(By.ID, "robotCheckbox")
#     checkbox.click()
#
#     #скроллим до checkbox
#     browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
#
#     radiobutton = browser.find_element(By.ID, "robotsRule")
#     radiobutton.click()
#
#     button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
#     button.click()
#
#
# finally:
#     time.sleep(6)
#     browser.quit()


"""
Загрузка файлов
Если нам понадобится загрузить файл на веб-странице, мы можем использовать 
уже знакомый нам метод send_keys. Только теперь нам нужно в качестве аргумента 
передать путь к нужному файлу на диске вместо простого текста.

Чтобы указать путь к файлу, можно использовать стандартный модуль Python 
для работы с операционной системой — os. В этом случае ваш код не будет 
зависеть от операционной системы, которую вы используете. Добавление файла 
будет работать и на Windows, и на Linux, и даже на MaсOS.

Пример кода, который позволяет указать путь к файлу 'file.txt', 
находящемуся в той же папке, что и скрипт, который вы запускаете:

import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
element.send_keys(file_path)

"""

# import os
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# try:
#     link = "https://suninjuly.github.io/file_input.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # заполняет текстовое поле
#     first_name = browser.find_element(By.NAME, "firstname")
#     first_name.send_keys("Евгений")
#
#     last_name = browser.find_element(By.NAME, "lastname")
#     last_name.send_keys("Пихтулов")
#
#     email = browser.find_element(By.NAME, "email")
#     email.send_keys("pigta@gmail.com")
#
#     element = browser.find_element(By.ID, "file")
#     current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
#     file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
#     element.send_keys(file_path)
#
#     button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
#     button.click()
#
# finally:
#     time.sleep(6)
#     browser.quit()

"""
аллерт
"""

"""
Теперь рассмотрим ситуацию, когда в сценарии теста возникает необходимость 
не только получить содержимое alert, но и нажать кнопку OK, чтобы закрыть alert. 
Alert является модальным окном: это означает, что пользователь не может 
взаимодействовать дальше с интерфейсом, пока не закроет alert. 
Для этого нужно сначала переключиться на окно с alert, а затем принять 
его с помощью команды accept():
"""

# alert = browser.switch_to.alert
# alert.accept()                          # закрытие аллерта

"""
Чтобы получить текст из alert, используйте свойство text объекта alert:
"""

# alert = browser.switch_to.alert
# alert_text = alert.text

"""
Другой вариант модального окна, который предлагает пользователю выбор 
согласиться с сообщением или отказаться от него, называется confirm. 
Для переключения на окно confirm используется та же команда, что и в случае с alert:
"""

# confirm = browser.switch_to.alert
# confirm.accept()
#
# #Для confirm-окон можно использовать следующий метод для отказа:
#
# confirm.dismiss()

"""
Третий вариант модального окна — prompt — имеет дополнительное поле для ввода текста. 
Чтобы ввести текст, используйте метод send_keys():
"""

# prompt = browser.switch_to.alert
# prompt.send_keys("My answer")
# prompt.accept()


"""
Задание: принимаем alert
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу https://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
Если все сделано правильно и достаточно быстро 
(в этой задаче тоже есть ограничение по времени), 
вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.

"""
# import math
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# try:
#     link = "https://suninjuly.github.io/alert_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
#     button.click()
#
#     alert = browser.switch_to.alert
#     alert.accept()
#
#     text_elt = browser.find_element(By.ID, "input_value")
#     x = text_elt.text
#     result = str(math.log(abs(12 * math.sin(int(x)))))
#
#     input1 = browser.find_element(By.ID, "answer")
#     input1.send_keys(result)
#
#     button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
#     button.click()
#
# finally:
#     time.sleep(6)
#     browser.quit()


"""
-------------------------------------------------------------------------------------------
Переход на новую вкладку браузера
-------------------------------------------------------------------------------------------
При работе с веб-приложениями приходится переходить по ссылкам, 
которые открываются в новой вкладке браузера. WebDriver может работать только 
с одной вкладкой браузера. При открытии новой вкладки WebDriver продолжит 
работать со старой вкладкой. Для переключения на новую вкладку надо явно указать, 
на какую вкладку мы хотим перейти. Это делается с помощью команды switch_to.window:
"""
#browser.switch_to.window(window_name)
"""
Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, 
который возвращает массив имён всех вкладок. Зная, что в браузере теперь открыто 
две вкладки, выбираем вторую вкладку:
"""
#new_window = browser.window_handles[1]
"""
Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
"""
#first_window = browser.window_handles[0]
"""
После переключения на новую вкладку поиск и взаимодействие с элементами будут происходить уже на новой странице.
"""

"""
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:

+Открыть страницу https://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
Если все сделано правильно и достаточно быстро 
(в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. 
Отправьте полученное число в качестве ответа на это задание.
"""
# import math
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# try:
#     link = "https://suninjuly.github.io/redirect_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")
#     button.click()
#
#     new_window = browser.window_handles[1]
#     browser.switch_to.window(new_window)
#
#     text_elt = browser.find_element(By.ID, "input_value")
#     x = text_elt.text
#     result = str(math.log(abs(12 * math.sin(int(x)))))
#
#     input1 = browser.find_element(By.ID, "answer")
#     input1.send_keys(result)
#
#     button2 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
#     button2.click()
#
# finally:
#     time.sleep(7)
#     browser.quit()



































