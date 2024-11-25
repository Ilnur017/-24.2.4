import pytest
from app.calculator import Calculator


class TestCalculator:
    def setup(self):
        self.calc = Calculator()

    def test_multiply(self):
        assert self.calc.multiply(5, 3) == 15  # Умножение

    def test_division(self):
        assert self.calc.division(10, 2) == 5  # Деление

    def test_subtraction(self):
        assert self.calc.subtraction(10, 4) == 6  # Вычитание

    def test_adding(self):
        assert self.calc.adding(7, 3) == 10  # Сложение
