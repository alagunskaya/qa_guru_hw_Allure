import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.page_load_strategy = 'eager'

    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()


@pytest.fixture
def calculator_page(driver):
    from calculator_page import CalculatorPage
    return CalculatorPage(driver)


@pytest.fixture
def test_data(request):
    # косвенная параметризация
    num1, operation, num2, expected = request.param

    if isinstance(num1, float):
        num1 = round(num1, 1)

    if isinstance(num2, float):
        num2 = round(num2, 1)

    return {
        'num1': num1,
        'operation': operation,
        'num2': num2,
        'expected': expected,
        'description': f"{num1} {operation} {num2} = {expected}"
    }


@pytest.fixture
def scenario_data(request):
    scenarios = {
        'addition': {'operation': 'add', 'result_sign': 'положительный'},
        'subtract': {'operation': 'sub', 'result_sign': 'может быть отрицательным'},
        'multiply': {'operation': 'mult', 'result_sign': 'зависит от знаков'},
        'divide': {'operation': 'div', 'result_sign': 'может быть дробным'},
    }

    scenario_name = request.param
    return scenarios.get(scenario_name, {})
