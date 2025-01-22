from selenium.webdriver.common.by import By

class LocatorsBase:
    FIRST_ORDER_BUTTON = [By.CLASS_NAME, 'Button_Button__ra12g']
    SECOND_ORDER_BUTTON = [By.XPATH, '//button[@class="Button_Button__ra12g Button_UltraBig__UU3Lp"]']
    BASE_PAGE_BUTTON = [By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]']
    YANDEX_PAGE_BUTTON = [By.XPATH, '//a[@class="Header_LogoYandex__3TSOI"]']