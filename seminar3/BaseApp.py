from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage: #базовый класс страниц

    def __init__(self,driver): #конструктору передадим драйвер из фикстур
        self.driver = driver
        self.base_url = 'https://test-stand.gb.ru'


    def find_element(self, locator,time=10): #добавили ожидание и локатор вместо пути элемента
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),   #ждем появления элемента, обнаружнного по локатору
                message=f"Can't find element by locator {locator}") #сообщение, если элемент не будет найден, для отладки

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        return element.value_of_css_property(property)

    # метод открытия страницы с сайтом
    def go_to_site(self):
        return self.driver.get(self.base_url)