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

"""
Например, мы хотим найти кнопку со значением id="submit_button":
"""

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/simple_form_find_task.html")
# button = browser.find_element(By.ID, "submit_button")


"""
Поиск нескольких элементов
Вы можете столкнуться с ситуацией, когда на странице будет несколько элементов, 
подходящих под заданные вами параметры поиска. В этом случае WebDriver вернет 
вам только первый элемент, который встретит во время поиска по HTML. Если вам нужен не первый, 
а второй или следующие элементы, вам нужно либо задать более точный селектор для поиска, 
либо использовать методы 
find_elements, 
которые мы рассмотрим чуть позже.

Иногда в статьях про Selenium WebDriver вы также будете встречать 
термин "локаторы", под которым подразумеваются стратегии поиска и значения, 
по которым должен выполняться поиск. Например, можно искать по локатору By.ID 
со значением "send_button".
"""

"""
Работа с браузером в Selenium
Если вы уже пробовали запускать примеры скриптов, то могли заметить, 
что браузер не всегда закрывается после выполнения кода. 
Поэтому обратите внимание на то, что необходимо явно закрывать окно браузера в 
нашем коде при помощи команды browser.quit(). Каждый раз при открытии браузера 
browser = webdriver.Chrome() в системе создается процесс, который останется висеть, 
если вы вручную закроете окно браузера. Чтобы не остаться без оперативной памяти 
после запуска нескольких скриптов, всегда добавляйте к своим скриптам команду закрытия:

"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# link = "https://suninjuly.github.io/simple_form_find_task.html"
# browser = webdriver.Chrome()
# browser.get(link)
# button = browser.find_element(By.ID, "submit_button")
# button.click()
#
# # закрываем браузер после всех манипуляций
# browser.quit()


"""
Для того чтобы гарантировать закрытие, даже если произошла ошибка в 
предыдущих строках, проще всего использовать конструкцию try/finally: 

"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.ID, "submit_button")
#     button.click()
#
# finally:
#     # закрываем браузер после всех манипуляций
#     browser.quit()

"""
пример заполнения формы
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "https://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.NAME, "first_name")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.NAME, "firstname")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

"""
задача перейти по ссылке и заполнить форму
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "https://suninjuly.github.io/find_link_text"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     time.sleep(3)
#     link = browser.find_element(By.LINK_TEXT, "224592")
#     link.click()
#
#     input1 = browser.find_element(By.NAME, "first_name")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.NAME, "firstname")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


"""
Поиск всех необходимых элементов с помощью find_elements
Мы уже упоминали, что метод find_element возвращает только первый из всех элементов, 
которые подходят под условия поиска. Иногда возникает ситуация, когда у нас есть 
несколько одинаковых по сути объектов на странице, например, иконки товаров 
в корзине интернет-магазина. В тесте нам нужно проверить, что отображаются 
все выбранные для покупки товары. Для этого существует метод find_elements, 
которые в отличие от find_element вернёт список всех найденных элементов 
по заданному условию. Проверив длину списка, мы можем удостовериться, 
что в корзине отобразилось правильное количество товаров. Пример кода 
(код приведен только для примера, сайта fake-shop.com скорее всего не существует):

"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# подготовка для теста
# открываем страницу первого товара
# данный сайт не существует, этот код приведен только для примера

# browser.get("https://fake-shop.com/book1.html")
#
# # добавляем товар в корзину
# add_button = browser.find_element(By.CSS_SELECTOR, ".add")
# add_button.click()
#
# # открываем страницу второго товара
# browser.get("https://fake-shop.com/book2.html")
#
# # добавляем товар в корзину
# add_button = browser.find_element(By.CSS_SELECTOR, ".add")
# add_button.click()
#
# # тестовый сценарий
# # открываем корзину
# browser.get("https://fake-shop.com/basket.html")
#
# # ищем все добавленные товары
# goods = browser.find_elements(By.CSS_SELECTOR, ".good")
#
# # проверяем, что количество товаров равно 2
# assert len(goods) == 2

"""
заполняем форму через цикл фор
"""

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("https://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.TAG_NAME, "input")
#
#     for element in elements:
#         element.send_keys("евгеша")
#     time.sleep(10)
#     button = browser.find_element(By.TAG_NAME, "button")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла

"""
Задание: поиск элемента по XPath
На этот раз воспользуемся возможностью искать элементы по XPath. 

На странице https://suninjuly.github.io/find_xpath_form вы найдете такую же форму регистрации, 
как в шаге 3, при этом в нее добавилась куча одинаковых кнопок отправки.
Но сработает только кнопка с текстом "Submit", и наша задача нажать в коде именно на неё. 

Ваши шаги: 

В коде из шага 4 замените ссылку на  https://suninjuly.github.io/find_xpath_form.
Подберите уникальный XPath-селектор так, чтобы он находил только кнопку с текстом Submit. 
XPath можете формулировать как угодно (по тексту, по структуре, по атрибутам) - главное, 
чтобы он работал.
Модифицируйте код из шага 3 таким образом, чтобы поиск кнопки происходил с помощью XPath.
Запустите ваш код.
Если вы подобрали правильный селектор и все прошло хорошо, то вы получите код, 
который нужно отправить в качестве ответа на это задание.

"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("https://suninjuly.github.io/find_xpath_form")
#
#     input1 = browser.find_element(By.NAME, "first_name")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.NAME, "firstname")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[6]/button[3]")
#     button.click()
#
# finally:
#     time.sleep(7)
#     browser.quit()

"""
Уникальность селекторов: часть 1
Мы уже упоминали, что идеальный селектор — это такой селектор, 
который позволяет найти только один искомый элемент на странице. 
Благодаря уникальным селекторам наши тесты становятся стабильнее 
и меньше зависят от изменений в вёрстке страницы. Небольшие изменения 
разработчики делают достаточно часто, а мы бы не хотели постоянно исправлять наши тесты.

Другое важное замечание: хороший тест проверяет только маленькую, 
атомарную часть функциональности. Простые тесты, которые проверяют небольшой 
сценарий, лучше, чем один большой тест, проверяющий сразу много сценариев. 
Благодаря простым тестам мы быстрее локализуем место в продукте, где появился баг, 
а также можем найти одновременно несколько новых багов. Упавший большой автотест 
укажет только на первую встреченную проблему, так как он заканчивает работу при 
первой же найденной ошибке. В этом их отличие от ручных тестов, в которых мы, 
проверяя функциональность продукта по тест-кейсу, можем гибко обойти 
встречающиеся проблемы и пройти тест-кейс до конца, найдя все баги.

Рассмотрим следующий пример: у нас есть форма регистрации, в которой есть 
обязательные и необязательные поля для заполнения. Нужно проверить, что можно 
успешно зарегистрироваться на сайте.

Сценарий плохого автотеста:

1
Открыть страницу с формой
Заполнить все поля
Нажать кнопку "Регистрация"
Проверить, что есть сообщение об успешной регистрации


Лучше разбить предыдущий тест на набор более простых автотестов:
1
Открыть страницу с формой
Заполнить только обязательные поля
Нажать кнопку "Регистрация"
Проверить, что есть сообщение об успешной регистрации

2
Открыть страницу с формой
Заполнить все обязательные поля
Заполнить все необязательные поля
Нажать кнопку "Регистрация"
Проверить, что есть сообщение об успешной регистрации

3
Открыть страницу с формой
Заполнить только необязательные поля
Проверить, что кнопка "Регистрация" неактивна
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, "body > div.container > form > div.first_block > div.form-group.first_class > input")
    input1.send_keys("Евгений")
    input2 = browser.find_element(By.CSS_SELECTOR, "body > div.container > form > div.first_block > div.form-group.second_class > input")
    input2.send_keys("Пихтулов")
    input3 = browser.find_element(By.CSS_SELECTOR, "body > div.container > form > div.first_block > div.form-group.third_class > input")
    input3.send_keys("pihtulovevgeny@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()

"""
Как работать с элементами типа checkbox и radiobutton?
Checkbox (чекбокс или флажок) и radiobutton (радиобаттон или переключатель) — 
часто используемые в формах элементы. Основная разница между ними состоит в том, 
что флажки позволяют выбирать/отключать любой из представленных вариантов, 
а переключатели позволяют выбрать только один из вариантов. Далее мы будем называть 
эти элементы на англоязычный манер: checkbox и radiobutton.

Чтобы снять/поставить галочку в элементе типа checkbox или выбрать опцию 
из группы radiobuttons, надо указать WebDriver метод поиска элемента и 
выполнить для найденного элемента метод click():

option1 = browser.find_element(By.CSS_SELECTOR, "[value='python']")
option1.click()


Также вы можете увидеть тег label рядом с input. Этот тег используется, чтобы сделать кликабельным текст, который отображается рядом с флажком. Этот текст заключен внутри тега label. Элемент label связывается с элементом input с помощью атрибута for, в котором указывается значение атрибута id для элемента input:

<div>
  <input type="radio" id="python" name="language" checked>
  <label for="python">Python</label>
</div>
<div>
  <input type="radio" id="java" name="language">
  <label for="java">Java</label>
</div>
В этом случае можно также отметить нужный пункт с помощью WebDriver, выполнив метод click() на элементе label.

option1 = browser.find_element(By.CSS_SELECTOR, "[for='java']")
option1.click()

"""


"""
Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
Продолжим использовать силу роботов 🤖 для решения повседневных задач. 
На данной странице мы добавили капчу для роботов, то есть тест, являющийся 
простым для компьютера, но сложным для человека.

Ваша программа должна выполнить следующие шаги:

Открыть страницу https://suninjuly.github.io/math.html.
Считать значение для переменной x.
Посчитать математическую функцию от x (код для этого приведён ниже).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку Submit.

Для этой задачи вам понадобится использовать атрибут .text для найденного элемента. 
Обратите внимание, что скобки здесь не нужны:

x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
x = x_element.text
y = calc(x)

Атрибут text возвращает текст, который находится между открывающим 
и закрывающим тегами элемента. Например, text для данного элемента 
<div class="message">У вас новое сообщение</div> вернёт строку: "У вас новое сообщение".

Используйте функцию calc(), которая рассчитает и вернет вам значение функции, 
которое нужно ввести в текстовое поле. Не забудьте добавить этот код в начало вашего скрипта:

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Скопируйте его в поле ниже. 

"""
# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     link = "https://suninjuly.github.io/math.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     time.sleep(2)
#
#     welcome_text_elt = browser.find_element(By.ID, "input_value")
#     x = welcome_text_elt.text
#     result = str(math.log(abs(12 * math.sin(int(x)))))
#
#     input1 = browser.find_element(By.ID, "answer")
#     input1.send_keys(result)
#
#     checkbox = browser.find_element(By.ID, "robotCheckbox")
#     checkbox.click()
#
#     radiobutton = browser.find_element(By.ID, "robotsRule")
#     radiobutton.click()
#
#     button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()

"""
Метод get_attribute
Мы уже знаем, как найти нужный элемент на странице и как получить видимый пользователю текст. 
Для более детальных проверок в тесте нам может понадобиться узнать значение атрибута элемента.
Атрибуты могут быть стандартными свойствами, которые понимает и использует браузер 
для отображения и вёрстки элементов или для хранения служебной информации, 
например, name, width, height, color и многие другие. 
Также атрибуты могут быть созданы разработчиками проекта для задания собственных 
стилей или правил.

Значение атрибута представляет собой строку. Если значение атрибута отсутствует, 
то это равносильно значению атрибута равному "false". Давайте еще раз взглянем на 
страницу https://suninjuly.github.io/math.html. На ней есть radiobuttons, 
для которых выбрано значение по умолчанию. В автотесте нам может понадобиться проверить, 
что для одного из radiobutton по умолчанию уже выбрано значение. Для этого мы можем 
проверить значение атрибута checked у этого элемента. Вот HTML-код элемента:

<input class="check-input" type="radio" name="ruler" id="peopleRule" value="people" checked>

Найдём этот элемент с помощью WebDriver:
people_radio = browser.find_element(By.ID, "peopleRule")
Найдём атрибут "checked" с помощью встроенного метода get_attribute и проверим его значение:

people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"

Т.к. у данного атрибута значение не указано явно, 
то метод get_attribute вернёт "true". 
Возможно, вы заметили, что "true" написано с маленькой буквы, 
— все методы WebDriver взаимодействуют с браузером с помощью JavaScript, 
в котором булевые значения пишутся с маленькой буквы, а не с большой, как в Python.

Мы можем написать проверку другим способом, сравнив строки:

assert people_checked == "true", "People radio is not selected by default"
Если атрибута нет, то метод get_attribute вернёт значение None. 
Применим метод get_attribute ко второму radiobutton, и убедимся, что атрибут отсутствует.

robots_radio = browser.find_element(By.ID, "robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None

Так же мы можем проверять наличие атрибута disabled, который определяет, 
может ли пользователь взаимодействовать с элементом. Например, в предыдущем 
задании на странице с капчей для роботов JavaScript устанавливает атрибут 
disabled у кнопки Submit, когда истекает время, отведенное на решение задачи.

<button type="submit" class="btn btn-default" disabled>Submit</button>
"""

"""
Задание: поиск сокровища с помощью get_attribute
В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, 
как и в прошлом задании. Но теперь значение переменной х спрятано в "сундуке", 
точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.

Ваша программа должна:

Открыть страницу https://suninjuly.github.io/get_attribute.html.
Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
Посчитать математическую функцию от x (сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку "Submit".
Для вычисления значения выражения в п.4 используйте функцию calc(x) из предыдущей задачи.
"""
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)

    x_img = browser.find_element(By.ID, "treasure")
    x_value_img = x_img.get_attribute("valuex")

    result = str(math.log(abs(12 * math.sin(int(x_value_img)))))

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(result)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()























