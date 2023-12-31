import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage: #базовый класс страниц

    def __init__(self, driver: object) -> object: #конструктору передадим драйвер из фикстур
        self.driver = driver
        self.base_url = 'https://test-stand.gb.ru'


    def find_element(self, locator,time=10): #добавили ожидание и локатор вместо пути элемента
        try:
           element =  WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                   # ждем появления элемента, обнаружнного по локатору
                                                   message=f"Can't find element by locator {locator}")#сообщение, если элемент не будет найден, для отладки
        except:
            logging.exception("Find element exception")
            element = None
        return element

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.error(f"Property {property} not found in element with locator {locator}")
            return None
    # метод открытия страницы с сайтом
    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception("Exception while open site")
            start_browsing = None
        return start_browsing

    def alert(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            logging.exception("Exception with alert")
            return None
