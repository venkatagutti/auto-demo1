from selenium.webdriver.common.by import By


class HomePage():
    title_text_css_selector = '.title'

    def verify_is_logged_in(self, driver):
        text = driver.find_element(By.CSS_SELECTOR, self.title_text_css_selector).get_property('innerHTML')
        assert 'Products' in text
