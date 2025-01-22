from locators.locators_base import LocatorsBase
from locators.locators_questions import LocatorsQuestions

test_data_order = [
    (
        LocatorsBase.FIRST_ORDER_BUTTON, "Иван", "Петров", "Москва, ул. Пушкина, д. 10", '"Черкизовская"',
        "+79001234567",
        '"Choose четверг, 16-е января 2025 г."', '[1]'
    ),
    (
        LocatorsBase.FIRST_ORDER_BUTTON, "Мария", "Сидорова", "Москва, ул. Лермонтова, д. 5", '"Сокольники"',
        "+79007654321",
        '"Choose суббота, 18-е января 2025 г."', '[2]'
    ),
]

test_data_question = [
    (LocatorsQuestions.FIRST_QUESTION, LocatorsQuestions.FIRST_ANSWER, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    (LocatorsQuestions.SECOND_QUESTION, LocatorsQuestions.SECOND_ANSWER, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
    (LocatorsQuestions.THIRD_QUESTION, LocatorsQuestions.THIRD_ANSWER, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
    (LocatorsQuestions.FOURTH_QUESTION, LocatorsQuestions.FOURTH_ANSWER, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
    (LocatorsQuestions.FIFTH_QUESTION, LocatorsQuestions.FIFTH_ANSWER, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
    (LocatorsQuestions.SIX_QUESTION, LocatorsQuestions.SIX_ANSWER, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
    (LocatorsQuestions.SEVEN_QUESTION, LocatorsQuestions.SEVEN_ANSWER, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
    (LocatorsQuestions.EIGHT_QUESTION, LocatorsQuestions.EIGHT_ANSWER, "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
]
