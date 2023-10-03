from time import sleep

import requests
import yaml
from testpage import OperationsHelper, get, post, get_post
import logging

with open("./testdata.yaml",encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


def test_login_negative(browser):
    logging.info("Test login_negative Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401", "test_login_negative FAILED"


def test_login_positive(browser):
    logging.info("Test login_positive Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    assert testpage.login_success() == f"Hello, {testdata['login']}", "test_login_positive FAILED"


def test_add_post(browser):
    logging.info("Test add_post Starting")
    testpage = OperationsHelper(browser)
    # testpage.go_to_site()
    # testpage.enter_login(testdata["login"])
    # testpage.enter_pass(testdata["password"])
    # testpage.click_login_button()
    testpage.click_add_post_button()
    testpage.add_title(testdata["title"])
    testpage.add_description(testdata["description"])
    testpage.add_content(testdata["content"])
    testpage.click_save_button()
    sleep(1)
    assert testpage.new_post_title() == f"{testdata['title']}", "test add post FAILED!"


def test_contact_us(browser):
    logging.info("Test contact_us Starting")
    testpage = OperationsHelper(browser)
    # testpage.go_to_site()
    # testpage.enter_login(testdata["login"])
    # testpage.enter_pass(testdata["password"])
    # testpage.click_login_button()
    sleep(1)
    testpage.click_contact_button()
    testpage.add_name(testdata["u_name"])
    testpage.add_email(testdata["u_email"])
    testpage.add_contact_content(testdata["content_contact"])
    testpage.click_contact()
    assert testpage.alert() == "Form successfully submitted", "test contact us FAILED!"



def test_api_1(login):
    logging.info("Test api_1 Starting")
    res = get(login)
    lst = res['data']
    lst_id = [el["id"] for el in lst]

    assert 81591 in lst_id, 'тест провален'

def test_api_2(login):
    logging.info("Test api_2 Starting")
    my_post = post(login)
    all_posts = get_post(login)
    lst = all_posts['data']
    lst_description = [el["description"] for el in lst]

    assert "Post about the autotest task" in lst_description, 'тест провален'