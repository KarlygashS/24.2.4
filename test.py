import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator


    def test_multiply_success(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_division_success(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 6, 4) == 2

    def test_adding_success(self):
        assert self.calc.adding(self, 7, 7) == 14