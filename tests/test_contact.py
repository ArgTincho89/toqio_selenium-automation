from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.contact_page import ContactPage



class TestContact(BaseTest):
    
    def test_01_happy_path(self):
        """" 
        Being able to complete the "Contact us" form and submit it.
        """  
        # Opening the driver
        home_page = HomePage(self.driver)
        # Navigate to the "Contact us" page
        home_page.click(home_page.ContactUs)
        # Switching the focus to the new tab
        original_window = self.driver.current_window_handle
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        new_window = [window for window in self.driver.window_handles if window != original_window][0]
        self.driver.switch_to.window(new_window)
        # Creation of an "Contact us" instance
        contact_page = ContactPage(self.driver)
        # Acceptance of cookies
        contact_page.click(contact_page.cookies_consent_button)
        # Filling the form
        contact_page.set(contact_page.first_name_field, contact_page.first_name)
        contact_page.set(contact_page.last_name_field, contact_page.last_name)
        contact_page.set(contact_page.email_field, contact_page.email_address)
        contact_page.set(contact_page.phone_number_field, contact_page.phone_number)
        contact_page.set(contact_page.company_name_field, contact_page.company_name)
        contact_page.click_and_send_keys(contact_page.headquarter_selector, "DOWN", "ENTER")
        contact_page.click_and_send_keys(contact_page.heard_about_us_menu, "DOWN", "ENTER")
        contact_page.scroll_to_element(contact_page.privacy_policy_checkbox)
        contact_page.click(contact_page.privacy_policy_checkbox)
        contact_page.scroll_to_element(contact_page.send_button)
        contact_page.click(contact_page.send_button)
        success_message = contact_page.find(*contact_page.submited_message)
        assert success_message.is_displayed()
