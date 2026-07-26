import pytest
import allure
from calculator_page import CalculatorPage


@allure.feature("Веб-калькулятор")
@allure.story("Косвенная параметризация")
class TestCalculatorIndirect:

    @allure.title("Тестирование с десятичными числами")
    @pytest.mark.parametrize(
        "test_data",
        [(1.5000, 'add', 2.3, 3.8), (5.70, 'sub', 3.20, 2.5), (2.5, 'mult', 4.0, 10), (7.50, 'div', 2.5, 3), ],
        indirect=True, ids=["1.5 + 2.3 = 3.8", "5.7 - 3.2 = 2.5", "2.5 x 4.0 = 10", "7.5 / 2.5 = 3"])
    def test_decimal_operations(self, driver, test_data):
        page = CalculatorPage(driver)
        page.open()

        with allure.step(f"Вычисляем: {test_data['description']}"):
            page.compute(test_data['num1'], test_data['operation'], test_data['num2'])
            result = page.get_result()

        with allure.step(f"Проверяем результат: {test_data['description']}"):
            assert result == str(test_data['expected'])

    @allure.title("Тестирование по сценарию")
    @pytest.mark.parametrize(
        "scenario_data", ['addition', 'subtract', 'multiply', 'divide'],
        indirect=True, ids=["Scenario: addition", "Scenario: subtraction", "Scenario: multiplication", "Scenario: division"])
    def test_scenario_based(self, driver, scenario_data):
        page = CalculatorPage(driver)
        page.open()

        operation = scenario_data['operation']
        result_sign = scenario_data['result_sign']

        with allure.step(f"Выполняем операцию {operation} ({result_sign})"):
            page.compute(10, operation, 5)
            result = page.get_result()

        with allure.step("Проверяем, что результат получен"):
            assert result is not None
            allure.attach(f"Операция: {operation}\nРезультат: {result}\nХарактеристика: {result_sign}",
                          name="Информация о тесте", attachment_type=allure.attachment_type.TEXT)
