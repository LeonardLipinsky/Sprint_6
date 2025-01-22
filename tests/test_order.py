import allure
import pytest

from selenium import webdriver
from constants import URL_HOME_PAGE, URL_REDIRECT_PAGE
from data import test_data_order
from pages.order_page import OrderPage
from pages.question_page import QuestionPage

@allure.story('Test success creation of order')
class TestOrder:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.order_page = OrderPage(cls.driver)
        cls.question_page = QuestionPage(cls.driver)

    @allure.title('Follow the path of success order creation')
    @pytest.mark.parametrize(
        "order_button, first_name, last_name, address, subway_station, phone, date, time_index",
        test_data_order
    )
    def test_order_success(self, order_button, first_name, last_name, address, subway_station, phone, date, time_index):
        self.question_page.go_to_site()
        self.question_page.wait_for_load_faq_block()
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
        assert URL_HOME_PAGE in self.order_page.get_actual_url()
        self.order_page.click_yandex_button()
        assert URL_REDIRECT_PAGE in self.order_page.get_actual_url()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()



