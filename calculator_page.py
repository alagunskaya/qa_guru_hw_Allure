from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


class CalculatorPage:
    BUTTON_0 = (By.NAME, "zero")
    BUTTON_1 = (By.NAME, "one")
    BUTTON_2 = (By.NAME, "two")
    BUTTON_3 = (By.NAME, "three")
    BUTTON_4 = (By.NAME, "four")
    BUTTON_5 = (By.NAME, "five")
    BUTTON_6 = (By.NAME, "six")
    BUTTON_7 = (By.NAME, "seven")
    BUTTON_8 = (By.NAME, "eight")
    BUTTON_9 = (By.NAME, "nine")

    BUTTON_ADD = (By.NAME, "add")
    BUTTON_SUBTRACT = (By.NAME, "subtract")
    BUTTON_MULTIPLY = (By.NAME, "multiply")
    BUTTON_DIVIDE = (By.NAME, "divide")

    BUTTON_EQUAL = (By.NAME, "calculate")
    BUTTON_CLEAR = (By.NAME, "clearButton")
    BUTTON_DECIMAL = (By.XPATH, "//input[@name='decimal' and @value='.']")
    DISPLAY = (By.ID, "display")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    def open(self):
        with allure.step("Открываем страницу калькулятора"):
            self.driver.get("https://www.theonlinecalculator.com/")
        return self

    def click_digit(self, digit):
        with allure.step(f"Нажимаем цифру {digit}"):
            if digit == 0:
                self.wait.until(EC.element_to_be_clickable(self.BUTTON_0)).click()
            elif digit == 1:
                self.wait.until(EC.element_to_be_clickable(self.BUTTON_1)).click()
            elif digit == 2:
                self.wait.until(EC.element_to_be_clickable(self.BUTTON_2)).click()
            elif digit == 3:
                self.wait.until(EC.element_to_be_clickable(self.BUTTON_3)).click()
            elif digit == 4:
                self.wait.until(EC.element_to_be_clickable(self.BUTTON_4)).click()
            elif digit == 5:
                self.wait.until(EC.element_to_be_clickable(self.BUTTON_5)).click()
            elif digit == 6:
                self.wait.until(EC.element_to_be_clickable(self.BUTTON_6)).click()
            elif digit == 7:
                self.wait.until(EC.element_to_be_clickable(self.BUTTON_7)).click()
            elif digit == 8:
                self.wait.until(EC.element_to_be_clickable(self.BUTTON_8)).click()
            elif digit == 9:
                self.wait.until(EC.element_to_be_clickable(self.BUTTON_9)).click()
        return self

    def click_decimal(self):
        with allure.step("Нажимаем десятичную точку"):
            self.wait.until(EC.element_to_be_clickable(self.BUTTON_DECIMAL)).click()
        return self

    def click_operation(self, operation):
        with allure.step(f"Нажимаем операцию {operation}"):
            if operation == 'add':
                self.wait.until(EC.element_to_be_clickable(self.BUTTON_ADD)).click()
            elif operation == 'sub':
                self.wait.until(EC.element_to_be_clickable(self.BUTTON_SUBTRACT)).click()
            elif operation == 'mult':
                self.wait.until(EC.element_to_be_clickable(self.BUTTON_MULTIPLY)).click()
            elif operation == 'div':
                self.wait.until(EC.element_to_be_clickable(self.BUTTON_DIVIDE)).click()
        return self

    def click_equal(self):
        with allure.step("Нажимаем кнопку равно"):
            self.wait.until(EC.element_to_be_clickable(self.BUTTON_EQUAL)).click()
        return self

    def clear(self):
        with allure.step("Очищаем калькулятор"):
            self.wait.until(EC.element_to_be_clickable(self.BUTTON_CLEAR)).click()
        return self

    def enter_number(self, number):
        with allure.step(f"Вводим число {number}"):
            num_str = str(number)

            for char in num_str:
                if char == '.':
                    self.click_decimal()
                else:
                    self.click_digit(int(char))
        return self

    def get_result(self):
        with allure.step("Получаем результат"):
            result = self.wait.until(EC.presence_of_element_located(self.DISPLAY)).get_attribute("value")
            return result

    def compute(self, num1, operation, num2):
        with allure.step(f"Вычисляем {num1} {operation} {num2}"):
            self.enter_number(num1)
            self.click_operation(operation)
            self.enter_number(num2)
            self.click_equal()
            return self.get_result()
