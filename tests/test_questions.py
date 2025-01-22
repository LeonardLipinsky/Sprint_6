import allure
import pytest
from selenium import webdriver

from data import test_data_question
from pages.base_page import BasePage
from pages.question_page import QuestionPage

@allure.story('Test question contains correct answer')
class TestQuestion:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.base_page = BasePage(cls.driver)
        cls.question_page = QuestionPage(cls.driver)

    @allure.title('Assert actual answer text with expected')
    @pytest.mark.parametrize(
        "locator_question, locator_answer, answer_text",
        test_data_question
    )
    def test_question(self, locator_question, locator_answer, answer_text):
        self.question_page.go_to_site()

        self.question_page.wait_for_load_faq_block()

        self.question_page.click_on_rcc()

        self.question_page.click_on_question(locator_question)

        answer = self.question_page.get_answer(locator_answer)

        assert answer == answer_text

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

