import pytest

from calculator import *

class TestCalculator:
    @pytest.fixture
    def calculator(self):
        return Calculator()

    def test_summa(self, calculator):
        assert calculator.summa(2, 5) == 7
        assert calculator.summa(2, 6) == 8

    def test_minus(self, calculator):
        assert calculator.minus(5, 5) == 1
        assert calculator.minus(5, 3) == 2

    def test_multi(self, calculator):
        assert calculator.multi(5, 5) == 25
        assert calculator.multi(5, 3) == 15

    def test_divide(self, calculator):
        assert calculator.divide(5, 5) == 1
        assert calculator.divide(6, 3) == 2
        with pytest.raises(ValueError, match="деление на ноль"):
            calculator.divide(10, 0)

    def test_is_even(self, calculator):
        assert calculator.is_even(5) == False
        assert calculator.is_even(4) == True






