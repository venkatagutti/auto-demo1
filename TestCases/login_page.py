from selenium.webdriver.common.by import By
import home_page


class LoginPage():
    username_css_selector = '#user-name'
    password_css_selector = '#password'
    login_button_css_selector = '#login-button'
    error_msg_css_selector = '.error-message-container > h3:nth-child(1)'
    hp = home_page.HomePage()

    def login(self, driver, username, password, is_login=True):
        driver.find_element(By.CSS_SELECTOR, self.username_css_selector).send_keys(username)
        driver.find_element(By.CSS_SELECTOR, self.password_css_selector).send_keys(password)
        driver.find_element(By.CSS_SELECTOR, self.login_button_css_selector).click()
        if is_login:
            self.hp.verify_is_logged_in(driver=driver)
        else:
            text = driver.find_element(By.CSS_SELECTOR, self.error_msg_css_selector).get_property('innerHTML')
            assert 'Epic sadface: Sorry, this user has been locked out.' in text
