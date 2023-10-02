from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")

    LOCATOR_BLOG = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_BUTTON_POST_CREATE = (By.CSS_SELECTOR, """#create-btn""")
    LOCATOR_TITLE_POST_CREATE = (By.XPATH, """//*[@id ="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_BUTTON_SAVE_POST = (By.XPATH, """//button[@type='submit'][@form='create-item']//span[@class='mdc-button__label']""")
    LOCATOR_NEW_POST = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")

    LOCATOR_BUTTON_CONTACT = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_INPUT_NAME = (By.XPATH,"""//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_INPUT_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_INPUT_CONTENT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_BUTTON_CONTACT_US = (By.CSS_SELECTOR,"""button""")



class OperationsHelper(BasePage):
    def enter_login(self, word): #ввод логина
        logging.info(f"Send {word} to element{TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)  #ищем поле
        login_field.clear()  #очищаем поле
        login_field.send_keys(word)

    def enter_pass(self, word): #ввод пароля
        logging.info(f"Send {word} to element{TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)  #ищем поле
        login_field.clear()  #очищаем поле
        login_field.send_keys(word)

    def click_login_button(self): #нажатие кнопки
        logging.info(f"Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

       # функция, которая возвращает текст в элементе с ошибкой
    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2) #ищем поле
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_blog(self):
        blog = self.find_element(TestSearchLocators.LOCATOR_BLOG)
        text = blog.text
        logging.info(f"Нашли текст *{text}* локатор Блог")
        return text

    def click_button_create_post(self): #нажатие кнопки создания поста странице Блог
        logging.info(f"Click create post button")
        self.find_element(TestSearchLocators.LOCATOR_BUTTON_POST_CREATE).click()

    def input_title_post(self, word): #ввод название поста
        logging.info(f"Send {word} to element{TestSearchLocators.LOCATOR_TITLE_POST_CREATE[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_TITLE_POST_CREATE)  #ищем поле
        login_field.clear()  #очищаем поле
        login_field.send_keys(word)

    def click_button_save_post(self): #нажатие кнопки сохранения поста на странице создания поста
        logging.info(f"Click save post button")
        self.find_element(TestSearchLocators.LOCATOR_BUTTON_SAVE_POST).click()

    def new_post(self):
        post = self.find_element(TestSearchLocators.LOCATOR_NEW_POST)
        text = post.text
        logging.info(f"Нашли текст *{text}* локатор Пост")
        return text

    def click_contact(self): #нажатие Contact Us
        logging.info(f"Click Contact")
        self.find_element(TestSearchLocators.LOCATOR_BUTTON_CONTACT).click()

    def input_name(self, word):  # ввод имени в форму Contact us!
        logging.info(f"Send {word} to element{TestSearchLocators.LOCATOR_INPUT_NAME[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_NAME)  # ищем поле
        login_field.clear()  # очищаем поле
        login_field.send_keys(word)

    def input_email(self, word):  # ввод email в форму Contact us!
        logging.info(f"Send {word} to element{TestSearchLocators.LOCATOR_INPUT_EMAIL[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_EMAIL)  # ищем поле
        login_field.clear()  # очищаем поле
        login_field.send_keys(word)

    def input_content(self, word):  # ввод content в форму Contact us!
        logging.info(f"Send {word} to element{TestSearchLocators.LOCATOR_INPUT_CONTENT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_CONTENT)  # ищем поле
        login_field.clear()  # очищаем поле
        login_field.send_keys(word)

    def click_button_contact_us(self):
        logging.info(f"Click button Contact Us")
        self.find_element(TestSearchLocators.LOCATOR_BUTTON_CONTACT_US).click()

    def alert(self):
        logging.info("Get alert message")
        alert = self.driver.switch_to.alert
        return alert.text


