import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, locator):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, locator)))
        except Exception as error:
            print(f"find_element 에러 발생: {error}")

    def click(self, by, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, locator)))
            actions = ActionChains(self.driver)
            actions.click(element).perform()
            time.sleep(1)
        except Exception as error:
            print(f"click 에러 발생: {error}")

    def send_keys(self, by, locator, text):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, locator)))
            element = self.find_element(by, locator)
            element.send_keys(text)
            time.sleep(1)
        except Exception as error:
            print(f"send_keys 에러 발생: {error}")

    def get_text(self, by, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, locator)))
            element = self.find_element(by, locator)
            return element.text
        except Exception as error:
            print(f"get_text 에러 발생: {error}")

    def move_scroll(self, by, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, locator)))
            element = self.find_element(by, locator)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(1)
        except Exception as error:
            print(f"move_scroll 에러 발생: {error}")

    def assert_text(self, by, locator, text):
        try:
            elementText = self.find_element(by, locator).text
            if elementText == text:
                assert True
            else:
                print(f"acutal Text: {elementText}, expected Text: {text}")
                assert False
        except Exception as error:
            print(f"assert_text 에러 발생: {error}")
