from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage



class ContactPage(BasePage):
    
    # Contact page element locators
    first_name_field = (By.CSS_SELECTOR, "input[name='firstname']")
    last_name_field = (By.CSS_SELECTOR, "input[name='lastname']")
    email_field = (By.CSS_SELECTOR, "input[name='email']")
    phone_number_field = (By.CSS_SELECTOR, "input[name='phone']")
    company_name_field = (By.CSS_SELECTOR, "input[name='company']")
    headquarter_selector = (By.CSS_SELECTOR, "select[name='location_of_headquarters']")
    heard_about_us_menu = (By.CSS_SELECTOR, "select[name='how_did_you_hear_about_us_']")
    privacy_policy_checkbox = (By.CSS_SELECTOR, "#hsForm_45092bb0-9980-45b3-bf08-01bc672cf116_2852 > fieldset:nth-child(10) > div > div:nth-child(1) > div input")
    send_button = (By.CSS_SELECTOR, "div.hs_submit input")
    cookies_consent_button = (By.CSS_SELECTOR, "button#hs-eu-confirmation-button")
    submited_message = (By.CSS_SELECTOR, "div.submitted-message")
    
    
    # Variables for Contact Form
    first_name = "FirstName"
    last_name = "LastName"
    email_address = "user@companyx.com"
    company_name = "CompanyX LTD"
    phone_number = "1122334455"
    
    
    # Methods for Contact Page
    def set(self, locator, value):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)
        
        
    def click_and_send_keys(self, locator, *keys):
        # Clicks an element a permorms keyboard actions.
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()
        
        keys_mapping = {
            "DOWN": Keys.DOWN,
            "ENTER": Keys.ENTER,
            "UP": Keys.UP,
            "LEFT": Keys.LEFT,
            "RIGHT": Keys.RIGHT,
            "SPACE": Keys.SPACE,
        }
        
        for key in keys:
            if key in keys_mapping:
                element.send_keys(keys_mapping[key])
            else:
                print(f"Key '{key}' not recognized.")
        
            
    
    def __init__(self, driver):
        super().__init__(driver)
        
   