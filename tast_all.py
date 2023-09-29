"""Доработать пример из лекции следующим образом:
вынести все локаторы элементов в фикстуры в conftest.py
вынести ожидаемый результат в фикстуру в conftest.py
добавить завершение работы Selenium после теста
вынести время ожидания в конфигурационный файл testdata.yaml"""

"""Доработать программу, полученную в предыдущем задании
добавив туда шаг, в котором будет проверяться успешность
входа пользователя при вводе верного имени и пароля.
Имя и пароль должны храниться в конфигурационном файле."""

"""Домашнее Задание 
Добавить в тестовый проект шаг добавления
поста после входа. Должна выполняться
проверка на наличие названия поста на странице
сразу после его создания."""

import yaml
import conftest
from module import Site
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

#site = Site(testdata["address"])

def test_step1(site):
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
    err_label = site.find_element("xpath", x_selector3)
    assert err_label.text == "401"


def test_step2(site, selector_input_login, selector_input_password, selector_button, selector_error):
    input1 = site.find_element("xpath", selector_input_login)
    input1.send_keys("test")
    input2 = site.find_element("xpath", selector_input_password)
    input2.send_keys("test")
    btn = site.find_element("css", selector_button)
    btn.click()
    err_label = site.find_element("xpath", selector_error)
    assert err_label.text == "401"


def test_step3(site, selector_input_login, selector_input_password, selector_button, selector_blog):
    input1 = site.find_element("xpath", selector_input_login)
    input1.clear()
    input1.send_keys(testdata['login'])
    input2 = site.find_element("xpath", selector_input_password)
    input2.clear()
    input2.send_keys(testdata['password'])
    btn = site.find_element("css", selector_button)
    btn.click()
    blog = site.find_element("xpath", selector_blog)
    assert blog.text == "Blog"

def test_step4(site, selector_input_login, selector_input_password, selector_button, selector_create_post,
               selector_button_create_post, selector_input_title,
               selector_button_save, selector_new_post):
    input1 = site.find_element("xpath", selector_input_login)
    input1.clear()
    input1.send_keys(testdata['login'])
    input2 = site.find_element("xpath", selector_input_password)
    input2.clear()
    input2.send_keys(testdata['password'])

    btn = site.find_element("css", selector_button)
    btn.click()

    btn = site.find_element("css", selector_button_create_post)
    btn.click()

    input3 = site.find_element("xpath", selector_input_title)
    input3.clear()
    input3.send_keys(testdata['title'])

    btn = site.find_element("xpath", selector_button_save)
    time.sleep(5)
    btn.click()

    time.sleep(5)
    new_post = site.find_element('xpath', selector_new_post)

    assert new_post.text == "New post"