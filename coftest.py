import pytest
import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

@pytest.fixture()
def selector_input_login():
    return '//*[@id="login"]/div[1]/label/input'

@pytest.fixture()
def selector_input_password():
    return '//*[@id="login"]/div[2]/label/input'

@pytest.fixture()
def selector_button():
    return 'button'

@pytest.fixture()
def selector_error():
    return '//*[@id="app"]/main/div/div/div[2]/h2'

@pytest.fixture()
def selector_blog():
    return '//*[@id="app"]/main/div/div[1]/h1'

@pytest.fixture()
def site():
    site_instance = Site(testdata["address"])
    yield site_instance
    site_instance.driver.quit()

@pytest.fixture()
def selector_create_post():
    return '//*[@id="app"]/main/div/div/h1'

@pytest.fixture()
def selector_button_create_post():
    return '#create-btn'

@pytest.fixture()
def selector_input_title():
    return '//*[@id="create-item"]/div/div/div[1]/div/label/input'

@pytest.fixture()
def selector_button_save():
    return "//button[@type='submit'][@form='create-item']//span[@class='mdc-button__label']"

#"button[type='submit'][form='create-item'] .mdc-button__label"


@pytest.fixture()
def selector_new_post():
    return '//*[@id="app"]/main/div/div[1]/h1'