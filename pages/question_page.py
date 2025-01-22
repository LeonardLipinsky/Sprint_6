import allure
from selenium.common import WebDriverException

from locators.locators_questions import LocatorsQuestions
from pages.base_page import BasePage


class QuestionPage(BasePage):

    @allure.step('Set driver and get locators')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = LocatorsQuestions()

    def wait_for_load_faq_block(self):
        self.wait_for_load_block(self.locators.FIRST_QUESTION, 3)

    @allure.step('Close rcc window')
    def click_on_rcc(self):
        try:
            rcc = self.find_element(*self.locators.RCC)
            rcc.click()
        except WebDriverException:
            print("Элемент RCC не найден, пропускаем метод")


    @allure.step('Open question')
    def click_on_question(self, locator_question):
        first_question_base = self.find_element(*locator_question)
        first_question_base.click()

    @allure.step('Get answer text')
    def get_answer(self, locator_answer):
        return self.find_element(*locator_answer).text
