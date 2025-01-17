import time
from copy import deepcopy
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.webdriver import WebDriver
from locators.locators_order import LocatorsOrder
from locators.locators_base import LocatorsBase


class OrderPage:

    @allure.step('set driver and get locators')
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.locators_base = LocatorsBase()
        self.locators_order = LocatorsOrder()

    @allure.step('click on one of two order buttons')
    def click_order_button(self, button_locator):
        order_button = self.driver.find_element(*button_locator)
        order_button.click()

    @allure.step('Fill the name in themed field')
    def fill_first_name_field(self, name):
        first_name_field = self.driver.find_element(*self.locators_order.FIRST_NAME_FIELD)
        first_name_field.send_keys(name)

    @allure.step('Fill the last name in themed field')
    def fill_last_name_field(self, last_name):
        last_name_field = self.driver.find_element(*self.locators_order.LAST_NAME_FIELD)
        last_name_field.send_keys(last_name)

    @allure.step('Fill the address in themed field')
    def fill_address_field(self, address):
        address_field = self.driver.find_element(*self.locators_order.ADDRESS_FIELD)
        address_field.send_keys(address)

    @allure.step('Open subway list')
    def click_subway_field(self):
        subway_field = self.driver.find_element(*self.locators_order.SUBWAY_FIELD)
        subway_field.click()

    @allure.step('Select subway station from subway list')
    def select_subway_station(self, subway):
        locators_subway = deepcopy(self.locators_order.SUBWAY_SELECT)
        locators_subway[1] = locators_subway[1] + subway + "]"
        subway_station = self.driver.find_element(*locators_subway)
        subway_station.click()

    @allure.step('Fill the phone number in themed field')
    def fill_phone_field(self, phone_number):
        phone_field = self.driver.find_element(*self.locators_order.PHONE_FIELD)
        phone_field.send_keys(phone_number)

    @allure.step('Click on confirm button')
    def click_confirm_button(self):
        confirm_button = self.driver.find_element(*self.locators_order.CONFIRM_BUTTON)
        confirm_button.click()

    @allure.step('Open calendar')
    def click_date_field(self):
        date_field = self.driver.find_element(*self.locators_order.DATE_FIELD)
        date_field.click()

    @allure.step('Click on confirmation button')
    def click_order_button_variable(self):
        order_button = self.driver.find_element(*self.locators_order.ORDER_BUTTON)
        order_button.click()

    @allure.step('Click on order accept button')
    def click_order_accept_button(self):
        order_accept_button = self.driver.find_element(*self.locators_order.ORDER_ACCEPT_BUTTON)
        order_accept_button.click()

    @allure.step('Click to selected date in calendar')
    def select_date(self,date_day):
        locators_date = deepcopy(self.locators_order.DATE_SELECT)
        locators_date[1] = locators_date[1] + date_day + "]"
        date_select = self.driver.find_element(*locators_date)
        date_select.click()

    @allure.step('Open list with time schedule')
    def click_time_field(self):
        time_field = self.driver.find_element(*self.locators_order.TIME_FIELD)
        time_field.click()

    @allure.step('Select list from time schedule')
    def select_time(self, time_index):
        locators_time_index = deepcopy(self.locators_order.TIME_SELECT)
        locators_time_index[1] = locators_time_index[1] + time_index
        time_select = self.driver.find_element(*locators_time_index)
        time_select.click()

    @allure.step('Check text on success page')
    def verify_success_message(self):
        actual_text = self.driver.find_element(*self.locators_order.SUCCESS_MESSAGE).text
        return actual_text

    @allure.step('Click on order status button')
    def click_exit_order_button(self):
        exit_button = self.driver.find_element(*self.locators_order.EXIT_ORDER_BUTTON)
        exit_button.click()

    @allure.step('Click to get home page')
    def go_to_home(self):
        home_button = self.driver.find_element(*self.locators_order.HOME_BUTTON)
        home_button.click()

    @allure.step('Get actual url')
    def get_actual_url(self):
        actual_url = self.driver.current_url
        return  actual_url

    @allure.step('Click to get yandex page')
    def click_yandex_button(self):
        yandex_button = self.driver.find_element(*self.locators_order.YANDEX_BUTTON)
        yandex_button.click()
        all_tabs = self.driver.window_handles
        time.sleep(10)
        self.driver.switch_to.window(all_tabs[-1])

