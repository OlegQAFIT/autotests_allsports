from telnetlib import EC

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import allure
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from helpers import BasePage
from helpers.authorization import LoginPage
from locators.for_company_page_locators import CompanyPageLocators
from selenium.webdriver.support.ui import Select
import time


class Company(LoginPage, CompanyPageLocators, BasePage):

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

    @allure.step("Open SP")
    def open_sp(self):
        self.driver.get('https://xn--80akdrtu.xn--k1aahcehedi.xn--90ais/registration/bepaid')

    @allure.step("")
    def click_and_open_company_tab(self):
        self.hard_click(self.FOOTER_COMPANY)

    @allure.step("")
    def click_create_company_tab(self):
        self.hard_click(self.CREATE_COMPANY)

    @allure.step("")
    def drop_city_selection(self):
        location_dropdown = self.find_element(self.LOCATION_DROP_DOWN)
        select = Select(location_dropdown)
        select.select_by_visible_text("Minsk")

    @allure.step("")
    def drop_locale_selection(self):
        locale_dropdown = self.find_element(self.LOCALE_DROP_DOWN)
        select = Select(locale_dropdown)
        select.select_by_visible_text("ru")

    @allure.step("")
    def drop_timezone_selection(self):
        self.hard_click(self.TIMEZONE_DROP_DOWN)
        self.hard_click(self.MINSK_VALUE_TIMEZONE)

    @allure.step("")
    def drop_sell_strategy_selection(self):
        strategy_dropdown = self.find_element(self.SELL_STRATEGY_DROP_DOWN)
        select = Select(strategy_dropdown)
        select.select_by_visible_text("Country")

    @allure.step("")
    def drop_registration_type_selection(self):
        self.hard_click(self.REGISTRATION_TYPE_STANDARD)
        self.hard_click(self.REGISTRATION_TYPE_FORM)


    @allure.step("")
    def drop_registration_type_dropdown(self):
        registration_type_dropdown = self.find_element(self.dropdown)
        select = Select(registration_type_dropdown)
        select.select_by_visible_text("REGISTRATION_FORM")


    def drop_manager_selection(self):
        locale_dropdown = self.find_element(self.MANAGER_DROP_DOWN)
        select = Select(locale_dropdown)
        select.select_by_visible_text("QA-Oleg-A")

    def fill_fields(self):
        custom_name = self.faker.word()
        self.created_company_name = f"AT Company {custom_name}"
        self.company_input_value = self.created_company_name

        self.fill(CompanyPageLocators.COMPANY_INPUT, self.company_input_value)
        self.fill(CompanyPageLocators.LEGAL_NAME_INPUT, self.company_input_value)
        self.fill(CompanyPageLocators.VAT_NUMBER_INPUT, self.VAT_NUMBER_TEXT)
        self.fill(CompanyPageLocators.LEGAL_ADDRESS_INPUT, self.LEGAL_ADDRESS_TEXT)
        self.fill(CompanyPageLocators.CONTACT_PHONE_INPUT, self.CONTACT_PHONE_TEXT)


    def fill_fields_name_company(self):

        self.fill(CompanyPageLocators.COMPANY_INPUT, self.MAX_COMPANY_NAME_TEXT)
        self.fill(CompanyPageLocators.LEGAL_NAME_INPUT, self.MAX_COMPANY_NAME_TEXT)
        self.fill(CompanyPageLocators.VAT_NUMBER_INPUT, self.VAT_NUMBER_TEXT)
        self.fill(CompanyPageLocators.LEGAL_ADDRESS_INPUT, self.LEGAL_ADDRESS_TEXT)
        self.fill(CompanyPageLocators.CONTACT_PHONE_INPUT, self.CONTACT_PHONE_TEXT)


    def fill_fields_legal_name(self):
        custom_name = self.faker.word()
        self.created_company_name = f"AT Company {custom_name}"
        self.company_input_value = self.created_company_name

        self.fill(CompanyPageLocators.COMPANY_INPUT, self.company_input_value)
        self.fill(CompanyPageLocators.VAT_NUMBER_INPUT, self.VAT_NUMBER_TEXT)
        self.fill(CompanyPageLocators.LEGAL_ADDRESS_INPUT, self.LEGAL_ADDRESS_TEXT)
        self.fill(CompanyPageLocators.CONTACT_PHONE_INPUT, self.CONTACT_PHONE_TEXT)


    def fill_fields_vat_number(self):
        custom_name = self.faker.word()
        self.created_company_name = f"AT Company {custom_name}"
        self.company_input_value = self.created_company_name

        self.fill(CompanyPageLocators.COMPANY_INPUT, self.company_input_value)
        self.fill(CompanyPageLocators.VAT_NUMBER_INPUT, self.VAT_NUMBER_TEXT)
        self.fill(CompanyPageLocators.LEGAL_ADDRESS_INPUT, self.LEGAL_ADDRESS_TEXT)
        self.fill(CompanyPageLocators.CONTACT_PHONE_INPUT, self.CONTACT_PHONE_TEXT)


    def click_save_company(self):
        self.hard_click(self.SAVE_AND_CONTINUE_BUTTON)
        time.sleep(5)

    def assert_find_new_company(self):
        time.sleep(5)
        assert self.search_text_on_page(self.company_input_value), f"Текст '{self.company_input_value}' не найден на странице"


    def assert_found_elements_on_add_company_page(self):
        elements_to_check = [
            (self.ADD_COMPANY, 'Add company'),
            (self.HR_SETTINGS, 'HR SETTINGS'),
            (self.DATA_FOR_THE_CONTRACT, 'DATA FOR THE CONTRACT'),
            (self.BENEFIARY, 'BENEFIARY'),
            (self.OPTIONAL, 'OPTIONAL')
        ]

        for element, expected_text in elements_to_check:
            self.assert_element_text_equal(element, expected_text)


    def assert_found_errore_text(self):
        elements_to_check = [
            (self.ERRORE_TEXT, 'Количество символов в поле Имя не может превышать 191.'),
        ]

        for element, expected_text in elements_to_check:
            self.assert_element_text_equal(element, expected_text)

    def assert_found_errore_text_legal_name(self):
        elements_to_check = [
            (self.ERRORE_TEXT_LEGAL_NAME, 'Такое значение поля legal name уже существует.'),
        ]

        for element, expected_text in elements_to_check:
            self.assert_element_text_equal(element, expected_text)

    def assert_found_text_after_searching_vat_number(self):
        elements_to_check = [
            (self.ERRORE_TEXT_legal_name, 'Такое значение поля legal name уже существует.'),
        ]

        for element, expected_text in elements_to_check:
            self.assert_element_text_equal(element, expected_text)



    def assert_required_fields(self):
        elements_to_check = [
            (self.Locale_required_fields, 'Обязательное поле'),
            (self.Timezone_required_fields, 'Обязательное поле'),
            (self.Sell_Strategy_required_fields, 'Обязательное поле'),
            (self.Company_Name_required_fields, 'Обязательное поле'),
            (self.VAT_NUMBER_required_fields, 'Обязательное поле'),
            (self.Legal_Name_required_fields, 'Обязательное поле'),
            (self.Legal_Address_required_fields, 'Обязательное поле'),
            (self.Contact_Phone_required_fields, 'Обязательное поле')
        ]

        for element, expected_text in elements_to_check:
            self.assert_element_text_equal(element, expected_text)

    def assert_disable_elements(self):
        """
        Проверка, что элементы неактивны.
        """
        locators = ("compensation_amount", "DATE", "MIN_ORDER_ITEMS_INPUT")

        for locator in locators:
            input_element = self.driver.find_element(By.XPATH, getattr(CompanyPageLocators, locator))

            is_disabled = input_element.get_attribute('disabled')

            assert is_disabled is not None and is_disabled.lower() == 'true', f"Поле {locator} не задизэйблено"

    # def find_and_edit_company_by_name(self):
    #     # Поиск компании по названию
    #     company_xpath = f"//td[contains(text(), '{self.company_input_value}')]"
    #     company_element = self.find_element((By.XPATH, company_xpath))
    #
    #     # Получение родительского элемента строки (tr)
    #     company_row = company_element.find_element(By.xpath('..'))
    #
    #     # Нажатие на выпадающий список
    #     dropdown_button = company_row.find_element(By.XPATH, './/button')
    #     dropdown_button.click()
    #
    #     # Нажатие на кнопку "Редактировать"
    #     edit_button = company_row.find_element(By.XPATH, './/a[contains(text(), "Редактировать")]')
    #     edit_button.click()


    def assert_disable_elements_with_select_registration_type(self):
        compensation_amount_input = self.driver.find_element(By.XPATH, self.compensation_amount)
        date_input = self.driver.find_element(By.XPATH, self.DATE)
        min_order_items_input = self.driver.find_element(By.XPATH, self.MIN_ORDER_ITEMS_INPUT)

        assert not compensation_amount_input.is_enabled(), "Поле 'Compensation Amount' не задизейблено"
        assert not date_input.is_enabled(), "Поле 'Date' не задизейблено"
        assert not min_order_items_input.is_enabled(), "Поле 'Min Order Items' не задизейблено"


    def assert_disable_elements_in_new_company(self):
        id_amount_input = self.driver.find_element(By.XPATH, self.ID)
        compensation_amount_input = self.driver.find_element(By.XPATH, self.compensation_amount)
        date_input = self.driver.find_element(By.XPATH, self.DATE)
        min_order_items_input = self.driver.find_element(By.XPATH, self.MIN_ORDER_ITEMS_INPUT)

        assert not id_amount_input.is_enabled(), "Поле 'ID' не задизейблено"
        assert not compensation_amount_input.is_enabled(), "Поле 'Compensation Amount' не задизейблено"
        assert not date_input.is_enabled(), "Поле 'Date' не задизейблено"
        assert not min_order_items_input.is_enabled(), "Поле 'Min Order Items' не задизейблено"