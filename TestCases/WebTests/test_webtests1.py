import pytest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.core.utils import os_type
from selenium.webdriver.edge.service import Service
import login_page
from Libraries import config_ops


@pytest.fixture()
def browser_setup():
    driver_path = EdgeChromiumDriverManager(os_type=os_type()).install()
    service = Service(executable_path=driver_path)
    service.start()
    driver = webdriver.Edge(service=service)
    driver.get(url=config_ops.get_base_web_url())
    driver.maximize_window()
    driver.implicitly_wait(time_to_wait=30)
    yield driver
    driver.quit()


def test_mytest1(browser_setup):
    lp = login_page.LoginPage()
    lp.login(driver=browser_setup, username=config_ops.get_valid_user(), password=config_ops.get_password())


def test_mytest2(browser_setup):
    lp = login_page.LoginPage()
    lp.login(driver=browser_setup, username=config_ops.get_invalid_user(), password=config_ops.get_password(), is_login=False)

