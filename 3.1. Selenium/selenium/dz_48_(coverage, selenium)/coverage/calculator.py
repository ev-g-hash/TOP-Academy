class Calculator:
    def summa(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def multi(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("деление на ноль")
        return a / b

    def is_even(self, n):
        return n % 2 == 0
