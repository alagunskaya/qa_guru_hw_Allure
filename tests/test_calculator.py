import pytest
import allure
from calculator_page import CalculatorPage


@allure.feature("Веб-калькулятор")
class TestCalculator:

    @allure.title("Сложение: 5 + 3 = 8")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add(self, driver):
        page = CalculatorPage(driver)
        page.open()

        result = page.compute(5, 'add', 3)

        assert result == "8"

    @allure.title("Вычитание: 10 - 4 = 6")
    @allure.severity(allure.severity_level.NORMAL)
    def test_subtract(self, driver):
        page = CalculatorPage(driver)
        page.open()

        result = page.compute(10, 'sub', 4)

        assert result == "6"

    @allure.title("Умножение: 4 x 5 = 20")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_multiply(self, driver):
        page = CalculatorPage(driver)
        page.open()

        result = page.compute(4, 'mult', 5)

        assert result == "20"

    @allure.title("Деление: 15 / 3 = 5")
    @allure.severity(allure.severity_level.NORMAL)
    def test_divide(self, driver):
        page = CalculatorPage(driver)
        page.open()

        result = page.compute(15, 'div', 3)

        assert result == "5"

    @allure.title("Деление на ноль возвращает 'Not a Number'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_divide_by_zero(self, driver):
        page = CalculatorPage(driver)
        page.open()

        result = page.compute(10, 'div', 0)

        assert result == "Not a Number"

    @allure.title("Очистка калькулятора")
    def test_clear(self, driver):
        page = CalculatorPage(driver)
        page.open()

        with allure.step("Вводим число 123"):
            page.enter_number(123)

        with allure.step("Проверяем, что в поле 123"):
            result = page.get_result()
            assert result == "123"

        with allure.step("Очищаем калькулятор"):
            page.clear()

        with allure.step("Проверяем, что поле очистилось"):
            result = page.get_result()
            assert result == ""

        with allure.step("Вводим число 456"):
            page.enter_number(456)

        with allure.step("Проверяем, что в поле 456"):
            result = page.get_result()
            assert result == "456"

    @allure.title("Параметризованный тест всех операций")
    @pytest.mark.parametrize("num1, operation, num2, expected",
                             [(2, 'add', 3, 5), (10, 'sub', 4, 6), (3, 'mult', 4, 12), (15, 'div', 3, 5),
                              (0, 'add', 5, 5), (7, 'mult', 0, 0), ],
                             ids=["2 + 3 = 5", "10 - 4 = 6", "3 x 4 = 12", "15 / 3 = 5", "0 + 5 = 5", "7 x 0 = 0"])
    def test_all_operations(self, driver, num1, operation, num2, expected):
        page = CalculatorPage(driver)
        page.open()

        result = page.compute(num1, operation, num2)

        assert result == str(expected)

    @allure.title("Параметризованный тест деления на ноль")
    @pytest.mark.parametrize("num, expected", [
        (10, "Not a Number"),
        (100, "Not a Number"),
        pytest.param(0, "Not a Number", marks=pytest.mark.xfail(reason="bug")), ],
                             ids=["10 / 0 = Not a Number", "100 / 0 = 0", "0 / 0 != Not a Number"])
    def test_divide_by_zero_parameterized(self, driver, num, expected):
        page = CalculatorPage(driver)
        page.open()

        result = page.compute(num, 'div', 0)

        assert result == expected
