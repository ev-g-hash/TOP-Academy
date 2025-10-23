"""
с командной строки

python -m unittest test_my_file.py
"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_link(link):
    browser = webdriver.Chrome()
    browser.get(link)

    inpu = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
    inpu.send_keys("Евгений")
    inpu = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
    inpu.send_keys("Пихтулов")
    inpu = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
    inpu.send_keys("pihtulovevgeny@gmail.com")

class TestReg(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(test_link("http://suninjuly.github.io/registration1.html"),
                         "Вы зарегистрировались", "регистрация не удалась")

    # def test_reg2(self):
    #     self.assertEqual(test_link("http://suninjuly.github.io/registration2.html"),
    #                      "Вы зарегистрировались", "регистрация не удалась")

if __name__ == "__main__":
    unittest.main()






