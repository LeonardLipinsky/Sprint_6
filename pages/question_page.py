import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators_base import LocatorsBase
from locators.locators_questions import Locators


class QuestionPage:

    @allure.step('Set driver and get locators')
    def __init__(self, driver):
        self.driver = driver
        self.locators = Locators()

    @allure.step('Wait until home page opened')
    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.locators.FIRST_QUESTION))

    @allure.step('Close rcc window')
    def click_on_rcc(self):
        try:
            rcc = self.driver.find_element(*self.locators.RCC)
            rcc.click()
        except NoSuchElementException:
            print("Элемент RCC не найден, пропускаем метод")


    @allure.step('Open first question')
    def click_on_question_1(self):
        first_question_base = self.driver.find_element(*self.locators.FIRST_QUESTION)
        first_question_base.click()

    @allure.step('Open second question')
    def click_on_question_2(self):
        first_question_base = self.driver.find_element(*self.locators.SECOND_QUESTION)
        first_question_base.click()

    @allure.step('Open third question')
    def click_on_question_3(self):
        first_question_base = self.driver.find_element(*self.locators.THIRD_QUESTION)
        first_question_base.click()

    @allure.step('Open fourth question')
    def click_on_question_4(self):
        first_question_base = self.driver.find_element(*self.locators.FOURTH_QUESTION)
        first_question_base.click()

    @allure.step('Open fifth question')
    def click_on_question_5(self):
        first_question_base = self.driver.find_element(*self.locators.FIFTH_QUESTION)
        first_question_base.click()

    @allure.step('Open sixth question')
    def click_on_question_6(self):
        first_question_base = self.driver.find_element(*self.locators.SIX_QUESTION)
        first_question_base.click()

    @allure.step('Open seventh question')
    def click_on_question_7(self):
        first_question_base = self.driver.find_element(*self.locators.SEVEN_QUESTION)
        first_question_base.click()

    @allure.step('Open eights question')
    def click_on_question_8(self):
        first_question_base = self.driver.find_element(*self.locators.EIGHT_QUESTION)
        first_question_base.click()

    @allure.step('Get first answer text')
    def get_answer_1(self):
        return self.driver.find_element(*self.locators.FIRST_ANSWER).text

    @allure.step('Get second answer text')
    def get_answer_2(self):
        return self.driver.find_element(*self.locators.SECOND_ANSWER).text

    @allure.step('Get third answer text')
    def get_answer_3(self):
        return self.driver.find_element(*self.locators.THIRD_ANSWER).text

    @allure.step('Get fourth answer text')
    def get_answer_4(self):
        return self.driver.find_element(*self.locators.FOURTH_ANSWER).text

    @allure.step('Get fifth answer text')
    def get_answer_5(self):
        return self.driver.find_element(*self.locators.FIFTH_ANSWER).text

    @allure.step('Get sixth answer text')
    def get_answer_6(self):
        return self.driver.find_element(*self.locators.SIX_ANSWER).text

    @allure.step('Get seventh answer text')
    def get_answer_7(self):
        return self.driver.find_element(*self.locators.SEVEN_ANSWER).text

    @allure.step('Get eights answer text')
    def get_answer_8(self):
        return self.driver.find_element(*self.locators.EIGHT_ANSWER).text