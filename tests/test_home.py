import time

from tests.base_test import BaseTest
from pages.home_page import HomePage


class TestContact(BaseTest):
    
    def test_01_general_url_check(self):
        """
        Making sure the main URLs are functioning properly
        """
        # Opening the driver
        home_page = HomePage(self.driver)
        # Creation of an "Home page" instance
        home_page = HomePage(self.driver)
        # Acceptance of cookies
        home_page.click(home_page.cookies_consent_button)
        # Checking that all the main URLs are working when clicking on elements.
        home_page.click_and_verify_url(home_page.Platform)
        home_page.click_and_verify_url(home_page.UseCases)
        home_page.hover_over_element(home_page.Company)
        home_page.click_and_verify_url(home_page.AboutUs)
        home_page.hover_over_element(home_page.Company)
        home_page.click_and_verify_url(home_page.Newsroom)
        home_page.hover_over_element(home_page.Company)
        home_page.click_and_verify_url(home_page.Team)
        home_page.hover_over_element(home_page.Company)
        home_page.click_and_verify_url(home_page.Talent)
        home_page.hover_over_element(home_page.Company)
        home_page.click_and_verify_url(home_page.Contact)
        home_page.hover_over_element(home_page.Resources)
        home_page.click_and_verify_url(home_page.Insights)
        home_page.hover_over_element(home_page.Resources)
        home_page.click_and_verify_url(home_page.Podcast)
        home_page.click_and_verify_url(home_page.ContactUs)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        home_page.check_social_media(home_page.linkedin_button)
        home_page.check_social_media(home_page.x_button)
        home_page.check_social_media(home_page.youtube_button)
        