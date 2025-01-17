import allure
from selenium import webdriver
from pages.base_page import BasePage
from pages.question_page import QuestionPage

@allure.story('Test first question contains correct answer')
class TestQuestion1:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.base_page = BasePage(cls.driver)
        cls.question_page = QuestionPage(cls.driver)

    @allure.feature('Assert actual answer text with expected')
    def test_question_1(self):
        self.base_page.go_to_site()

        self.question_page.wait_for_load_home_page()

        self.question_page.click_on_rcc()

        self.question_page.click_on_question_1()

        answer_1 = self.question_page.get_answer_1()

        assert answer_1 == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

@allure.story('Test second question contains correct answer')
class TestQuestion2:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.base_page = BasePage(cls.driver)
        cls.question_page = QuestionPage(cls.driver)

    @allure.feature('Assert actual answer text with expected')
    def test_question_2(self):
        self.base_page.go_to_site()

        self.question_page.wait_for_load_home_page()

        self.question_page.click_on_rcc()

        self.question_page.click_on_question_2()

        answer_2 = self.question_page.get_answer_2()

        assert answer_2 == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

@allure.story('Test third question contains correct answer')
class TestQuestion3:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.base_page = BasePage(cls.driver)
        cls.question_page = QuestionPage(cls.driver)

    @allure.feature('Assert actual answer text with expected')
    def test_question_3(self):
        self.base_page.go_to_site()

        self.question_page.wait_for_load_home_page()

        self.question_page.click_on_rcc()

        self.question_page.click_on_question_3()

        answer_3 = self.question_page.get_answer_3()

        assert answer_3 == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

@allure.story('Test fourth question contains correct answer')
class TestQuestion4:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.base_page = BasePage(cls.driver)
        cls.question_page = QuestionPage(cls.driver)

    @allure.feature('Assert actual answer text with expected')
    def test_question_4(self):
        self.base_page.go_to_site()

        self.question_page.wait_for_load_home_page()

        self.question_page.click_on_rcc()

        self.question_page.click_on_question_4()

        answer_4 = self.question_page.get_answer_4()

        assert answer_4 == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

@allure.story('Test fifth question contains correct answer')
class TestQuestion5:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.base_page = BasePage(cls.driver)
        cls.question_page = QuestionPage(cls.driver)

    @allure.feature('Assert actual answer text with expected')
    def test_question_5(self):
        self.base_page.go_to_site()

        self.question_page.wait_for_load_home_page()

        self.question_page.click_on_rcc()

        self.question_page.click_on_question_5()

        answer_5 = self.question_page.get_answer_5()

        assert answer_5 == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

@allure.story('Test sixth question contains correct answer')
class TestQuestion6:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.base_page = BasePage(cls.driver)
        cls.question_page = QuestionPage(cls.driver)

    @allure.feature('Assert actual answer text with expected')
    def test_question_6(self):
        self.base_page.go_to_site()

        self.question_page.wait_for_load_home_page()

        self.question_page.click_on_rcc()

        self.question_page.click_on_question_6()

        answer_6 = self.question_page.get_answer_6()

        assert answer_6 == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

@allure.story('Test seventh question contains correct answer')
class TestQuestion7:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.base_page = BasePage(cls.driver)
        cls.question_page = QuestionPage(cls.driver)

    @allure.feature('Assert actual answer text with expected')
    def test_question_7(self):
        self.base_page.go_to_site()

        self.question_page.wait_for_load_home_page()

        self.question_page.click_on_rcc()

        self.question_page.click_on_question_7()

        answer_7 = self.question_page.get_answer_7()

        assert answer_7 == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

@allure.story('Test eights question contains correct answer')
class TestQuestion8:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.base_page = BasePage(cls.driver)
        cls.question_page = QuestionPage(cls.driver)

    @allure.feature('Assert actual answer text with expected')
    def test_question_8(self):
        self.base_page.go_to_site()

        self.question_page.wait_for_load_home_page()

        self.question_page.click_on_rcc()

        self.question_page.click_on_question_8()

        answer_8 = self.question_page.get_answer_8()

        assert answer_8 == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
