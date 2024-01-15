import allure
from faker import Faker
from helpers import BasePage
from helpers.authorization import LoginPage
from locators.for_company_page_locators import PortalUserLocators



class Company(LoginPage, PortalUserLocators, BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.faker = Faker()
        self.created_company_name = None
        self.company_input_value = None

    @allure.step("Open HR portal")
    def open_hr(self):
        self.driver.get('https://xn--e1affem4a.xn--k1aahcehedi.xn--90ais/login')

    @allure.step("Open Journal")
    def open_jn(self):
        self.driver.get('https://xn--d1aey.xn--k1aahcehedi.xn--90ais/login')


    @allure.step("Click and open Company tab")
    def click_and_open_company_tab(self):
        self.hard_click(self.FOOTER_COMPANY)