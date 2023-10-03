import time, yaml

import requests

from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

ids = dict()
with open("./locators.yaml") as f:
    locators = yaml.safe_load(f)
for locator in locators["xpath"].keys():
    ids[locator] = (By.XPATH, locators["xpath"][locator])
for locator in locators["css"].keys():
    ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])

with open('testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)

class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send '{word}' to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operate with {locator}")
            return False
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=2)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    # ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(ids["LOCATOR_PASS_FIELD"], word, description="password form")

    def add_title(self, string):
        self.enter_text_into_field(ids["LOCATOR_TITLE"], string, description="title")

    def add_description(self, string):
        self.enter_text_into_field(ids["LOCATOR_DESCRIPTION"], string, description="description")

    def add_content(self, string):
        self.enter_text_into_field(ids["LOCATOR_CONTENT"], string, description="description")

    def add_name(self, string):
        self.enter_text_into_field(ids["LOCATOR_CONTACT_NAME"], string, description="contact_name")

    def add_email(self, string):
        self.enter_text_into_field(ids["LOCATOR_CONTACT_EMAIL"], string, description="contact_email")

    def add_contact_content(self, string):
        self.enter_text_into_field(ids["LOCATOR_CONTACT_CONTENT"], string, description="contact_content")

# GET TEXT
    def new_post_title(self):
        return self.get_text_from_element(ids["LOCATOR_FIND_NEW_POST"], description="new_post_title")

    def get_error_text(self):
        return self.get_text_from_element(ids["LOCATOR_ERROR_FIELD"], description="error label")

    def login_success(self):
        return self.get_text_from_element(ids["LOCATOR_HELLO"], description="username")

    # def get_alert_message(self):
    #     time.sleep(2)
    #     logging.info("Get alert message")
    #     txt = self.get_alert_text()
    #     logging.debug(f"Alert message is {txt}")
    #     return txt
    def alert(self):
        time.sleep(2)
        logging.info("Get alert message")
        alert = self.driver.switch_to.alert
        return alert.text
# CLICK
    def click_save_button(self):
        self.click_button(ids["LOCATOR_SAVE_BTN"], description="save")

    def click_add_post_button(self):
        self.click_button(ids["LOCATOR_NEW_POST_BTN"], description="new post")

    def click_contact(self):
        self.click_button(ids["LOCATOR_CONTACT_SEND"], description="contact")

    def click_contact_button(self):
        self.click_button(ids["LOCATOR_CONTACT_BTN"], description="send")

    def click_login_button(self):
        self.click_button(ids["LOCATOR_LOGIN_BTN"], description="login")

#API
def get(token):
    try:
        resourсe = requests.get(testdata['url_posts'],
                            headers={'X-Auth-Token': token},
                            params={'owner': 'notMe'})
        if resourсe.status_code == 200:
            return resourсe.json()
        else:
            logging.error(f"Error with retrieving data. Status code: {resourсe.status_code}")
            return None
    except:
        logging.exception(f"Exception with get")
        return None

def post(token):
    try:
        new_post = requests.post(testdata['url_posts'],
                                data={'title': "New post",
                                'description': 'Post about the autotest task',
                                'content':'Add another test to the REST API task, in which a new post is created, \
                                 and then its presence on the server is checked by the "description" field'},
                                headers={'X-Auth-Token': token})
        if new_post.status_code == 200:
            return new_post.json()
        else:
            logging.error(f"Error with posting data. Status code: {new_post.status_code}")
            return None
    except:
        logging.exception(f"Exception with post")
        return None

def get_post(token):
    try:
        resourсe = requests.get(testdata['url_posts'],
                            headers={'X-Auth-Token': token})
        if resourсe.status_code == 200:
            return resourсe.json()
        else:
            logging.error(f"Error with retrieving data. Status code: {resourсe.status_code}")
            return None
    except Exception as e:
        logging.exception(f"Exception with get_post")
        return None