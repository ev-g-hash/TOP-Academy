from selenium import webdriver
import time
import unittest
import fact1
# import fact2


class Fact(unittest.TestCase):
    def test_fact1(self):
        self.assertEqual("button.btn", "button.btn", fact1.button)


    def test_fact2(self):
        self.assertEqual("Евгений", "Евгений", fact2.inpu.send_keys)


if __name__ == "__main__":
    unittest.main()






