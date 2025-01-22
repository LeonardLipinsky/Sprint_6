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


    @allure.step('Open first question')
    def click_on_question(self, locator_question):
        first_question_base = self.find_element(*locator_question)
        first_question_base.click()

    @allure.step('Open second question')
    def click_on_question_2(self):
        first_question_base = self.find_element(*self.locators.SECOND_QUESTION)
        first_question_base.click()

    @allure.step('Open third question')
    def click_on_question_3(self):
        first_question_base = self.find_element(*self.locators.THIRD_QUESTION)
        first_question_base.click()

    @allure.step('Open fourth question')
    def click_on_question_4(self):
        first_question_base = self.find_element(*self.locators.FOURTH_QUESTION)
        first_question_base.click()

    @allure.step('Open fifth question')
    def click_on_question_5(self):
        first_question_base = self.find_element(*self.locators.FIFTH_QUESTION)
        first_question_base.click()

    @allure.step('Open sixth question')
    def click_on_question_6(self):
        first_question_base = self.find_element(*self.locators.SIX_QUESTION)
        first_question_base.click()

    @allure.step('Open seventh question')
    def click_on_question_7(self):
        first_question_base = self.find_element(*self.locators.SEVEN_QUESTION)
        first_question_base.click()

    @allure.step('Open eights question')
    def click_on_question_8(self):
        first_question_base = self.find_element(*self.locators.EIGHT_QUESTION)
        first_question_base.click()

    @allure.step('Get first answer text')
    def get_answer(self, locator_answer):
        return self.find_element(*locator_answer).text

    @allure.step('Get second answer text')
    def get_answer_2(self):
        return self.find_element(*self.locators.SECOND_ANSWER).text

    @allure.step('Get third answer text')
    def get_answer_3(self):
        return self.find_element(*self.locators.THIRD_ANSWER).text

    @allure.step('Get fourth answer text')
    def get_answer_4(self):
        return self.find_element(*self.locators.FOURTH_ANSWER).text

    @allure.step('Get fifth answer text')
    def get_answer_5(self):
        return self.find_element(*self.locators.FIFTH_ANSWER).text

    @allure.step('Get sixth answer text')
    def get_answer_6(self):
        return self.find_element(*self.locators.SIX_ANSWER).text

    @allure.step('Get seventh answer text')
    def get_answer_7(self):
        return self.find_element(*self.locators.SEVEN_ANSWER).text

    @allure.step('Get eights answer text')
    def get_answer_8(self):
        return self.find_element(*self.locators.EIGHT_ANSWER).text