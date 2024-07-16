import logging
import requests

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    # The purpose of the BasePage is to contain methods common to all page objects
    def __init__(self, driver):
        self.driver = driver
        
        
    def find(self, *locator):
        # Finds an element
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
    
    
    def click(self, locator):
        # Clicks on an element
        clickable_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        clickable_element.click()
        
        
    def scroll_to_element(self, locator):
        # Scrolls to an element
        element = self.find(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        
        
    def hover_over_element(self, locator):
        # Hovers over an element
        element = self.find(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        
        
    def analyze_element(self, locator):
        # Grabs the url and target attributes of an element
        element = self.find(*locator)
        url = element.get_attribute('href')
        target_attribute = element.get_attribute('target')
        target = target_attribute is not None and target_attribute != ""
        print(f"url: {url}, target: {target}")
        return url, target
            
        
    def click_and_verify_url(self, locator):
        # Clicks on an element and verifies the redirection is correct, then goes back to where it was before.
        url, target = self.analyze_element(locator)
        element = self.find(*locator)
        element.click()
        if target:  # If target is True, then the link will open in a new tab
            logging.info("Target is true, expecting a new tab.")
            original_window = self.driver.current_window_handle
            WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
            new_window = [window for window in self.driver.window_handles if window != original_window][0]
            self.driver.switch_to.window(new_window)
            logging.info("Switched to the new window")
        else:  # If target is False, then the link will open in the same tab
            logging.info("Target is false, expecting the same tab.")
        # Verifying the URL is correct
        current_url = self.driver.current_url
        print(f" current url is {current_url}")
        assert current_url == url.split('?')[0], f"Expected URL {url}, but got {current_url}"
        # Verifying the status code is not a 4xx or 5xx error
        response = requests.head(url, allow_redirects=True)
        status_code = response.status_code
        assert 400 > status_code >= 200, f"Bad status code: {status_code}"
        logging.info(f"Response status for URL {url} is {status_code}")

        if target:
            logging.info("About to close the tab")
            self.driver.close()
            logging.info("Tab closed")
            self.driver.switch_to.window(original_window)
            logging.info("Switched back to the original window")
        else:
            self.driver.back()
            
            
    def check_social_media(self, locator):
        # Checks the social media buttons lead to correct URLs
        self.find(*locator).click()
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        original_window = self.driver.current_window_handle
        new_window = [window for window in self.driver.window_handles if window != original_window][0]
        self.driver.switch_to.window(new_window)
        logging.info("Switched to the new window.")
        # Verifying the URL is correct.
        current_url = self.driver.current_url
        print(f"Current URL is {current_url}")
        # Close the new tab and switch back to the original window.
        self.driver.close()
        logging.info("New tab closed.")
        self.driver.switch_to.window(original_window)
        logging.info("Switched back to the original window.")