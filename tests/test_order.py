import allure
import pytest
from selenium import webdriver
from locators.locators_base import LocatorsBase
from pages.base_page import BasePage
from pages.order_page import OrderPage
from pages.question_page import QuestionPage

@allure.story('Test success creation of order')
class TestOrder:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.base_page = BasePage(cls.driver)
        cls.order_page = OrderPage(cls.driver)
        cls.question_page = QuestionPage(cls.driver)

    @allure.feature('Follow the path of success order creation')
    @pytest.mark.parametrize(
        "order_button, first_name, last_name, address, subway_station, phone, date, time_index",
        [
            (
                    LocatorsBase.FIRST_ORDER_BUTTON, "Иван", "Петров", "Москва, ул. Пушкина, д. 10", '"Черкизовская"', "+79001234567",
                    '"Choose четверг, 16-е января 2025 г."', '[1]'
            ),
            (
                    LocatorsBase.FIRST_ORDER_BUTTON, "Мария", "Сидорова", "Москва, ул. Лермонтова, д. 5", '"Сокольники"', "+79007654321",
                    '"Choose суббота, 18-е января 2025 г."', '[2]'
            ),
        ]
    )
    def test_order_success(self, order_button, first_name, last_name, address, subway_station, phone, date, time_index):
        self.base_page.go_to_site()
        self.question_page.wait_for_load_home_page()
        self.question_page.click_on_rcc()
        self.order_page.click_order_button(order_button)
        self.order_page.fill_first_name_field(first_name)
        self.order_page.fill_last_name_field(last_name)
        self.order_page.fill_address_field(address)
        self.order_page.click_subway_field()
        self.order_page.select_subway_station(subway_station)
        self.order_page.fill_phone_field(phone)
        self.order_page.click_confirm_button()
        self.order_page.click_date_field()
        self.order_page.select_date(date)
        self.order_page.click_time_field()
        self.order_page.select_time(time_index)
        self.order_page.click_order_button_variable()
        self.order_page.click_order_accept_button()
        assert 'Заказ оформлен' in self.order_page.verify_success_message()
        self.order_page.click_exit_order_button()
        self.order_page.click_order_button(order_button)
        self.order_page.go_to_home()
        assert 'https://qa-scooter.praktikum-services.ru/' in self.order_page.get_actual_url()
        self.order_page.click_yandex_button()
        assert 'https://dzen.ru/?yredirect=true' in self.order_page.get_actual_url()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()



