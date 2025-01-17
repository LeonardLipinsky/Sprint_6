import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import URL_HOME_PAGE


class BasePage:
    @allure.step('set driver')
    def __init__(self, driver):
        self.driver = driver
        self.url = URL_HOME_PAGE

    @allure.step('open home page')
    def go_to_site(self):
        self.driver.get(self.url)

    @allure.step('find element')
    def find_element(self, locator, time=10):
        return self.driver.find_element(locator)

    @allure.step('find more than one elements')
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator), message=f'Not find elements {locator}')