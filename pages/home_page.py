
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    
    # Home page element locators
    Home = (By.CSS_SELECTOR, "div#hs_menu_wrapper_menu ul.active-branch li.hs-menu-item.hs-menu-depth-1.active.active-branch a")
    Platform = (By.CSS_SELECTOR, "#hs_menu_wrapper_menu > ul > li:nth-child(3) a")
    UseCases = (By.CSS_SELECTOR, "#hs_menu_wrapper_menu > ul > li:nth-child(4) a")
    Company = (By.CSS_SELECTOR, "#hs_menu_wrapper_menu > ul > li:nth-child(5) a")
    AboutUs = (By.CSS_SELECTOR, "#hs_menu_wrapper_menu > ul > li:nth-child(5) > ul > li:nth-child(2) > a")
    Newsroom = (By.CSS_SELECTOR, "#hs_menu_wrapper_menu > ul > li:nth-child(5) > ul > li:nth-child(3) > a")
    Team = (By.CSS_SELECTOR, "#hs_menu_wrapper_menu > ul > li:nth-child(5) > ul > li:nth-child(4) > a")
    Talent = (By.CSS_SELECTOR, "#hs_menu_wrapper_menu > ul > li:nth-child(5) > ul > li:nth-child(5) > a")
    Contact = (By.CSS_SELECTOR, "#hs_menu_wrapper_menu > ul > li:nth-child(5) > ul > li:nth-child(6) > a")
    Resources = (By.CSS_SELECTOR, "#hs_menu_wrapper_menu > ul > li:nth-child(6) a")
    Insights = (By.XPATH, "//*[@id='hs_menu_wrapper_menu']/ul/li[6]/ul/li[1]/a")
    Podcast = (By.XPATH, "//*[@id='hs_menu_wrapper_menu']/ul/li[6]/ul/li[2]/a")
    ContactUs = (By.ID, "hs-button_button")
    cookies_consent_button = (By.CSS_SELECTOR, "button#hs-eu-confirmation-button")
    linkedin_button = (By.CSS_SELECTOR, "#hs_cos_wrapper_footer_section__2 > footer > div > div > div > div.col-section.num5 > div > div > div:nth-child(1) > a")
    x_button = (By.CSS_SELECTOR, "#hs_cos_wrapper_footer_section__2 > footer > div > div > div > div.col-section.num5 > div > div > div:nth-child(2) > a")
    youtube_button = (By.CSS_SELECTOR, "#hs_cos_wrapper_footer_section__2 > footer > div > div > div > div.col-section.num5 > div > div > div:nth-child(3) > a")


    
    def __init__(self, driver):
        super().__init__(driver)