import allure
from pages.company import Company


@allure.feature('')
@allure.severity('')
@allure.story('')
def test_create_new_company_without_copay(driver):
    """
    Создание компании без copay
    """
    create_company = Company(driver)
    create_company.open_jn()
    create_company.login()
    create_company.click_and_open_company_tab()
    create_company.click_create_company_tab()
    create_company.drop_city_selection()
    create_company.drop_locale_selection()
    create_company.drop_timezone_selection()
    create_company.drop_sell_strategy_selection()
    create_company.drop_registration_type_selection()
    create_company.drop_manager_selection()
    create_company.fill_fields()
    create_company.click_save_company()
    create_company.click_and_open_company_tab()
    create_company.assert_find_new_company()


@allure.feature('')
@allure.severity('')
@allure.story('')
def test_create_new_company_with_copay(driver):
    """
    Создание компании с copay
    """
    create_company_with_copay = Company(driver)
    create_company_with_copay.open_jn()
    create_company_with_copay.login()
    create_company_with_copay.click_and_open_company_tab()
    create_company_with_copay.click_create_company_tab()
    create_company_with_copay.drop_city_selection()
    create_company_with_copay.drop_locale_selection()
    create_company_with_copay.drop_timezone_selection()
    create_company_with_copay.drop_sell_strategy_selection()
    create_company_with_copay.drop_registration_type_dropdown()
    create_company_with_copay.drop_manager_selection()
    create_company_with_copay.fill_fields()
    create_company_with_copay.click_save_company()
    create_company_with_copay.click_and_open_company_tab()
    create_company_with_copay.assert_find_new_company()


@allure.feature('')
@allure.severity('')
@allure.story('')
def test_disable_fields(driver):
    """
    Дизэйбл полей при copay
    """
    create_company = Company(driver)
    create_company.open_jn()
    create_company.login()
    create_company.click_and_open_company_tab()
    create_company.click_create_company_tab()
    create_company.drop_city_selection()
    create_company.drop_locale_selection()
    create_company.drop_timezone_selection()
    create_company.drop_sell_strategy_selection()
    create_company.drop_registration_type_dropdown()
    create_company.assert_disable_elements()


@allure.feature('')
@allure.severity('')
@allure.story('')
def test_found_actual_elements_on_add_company_page(driver):
    """
     Поиск элементов на странице
    """
    actual_elements = Company(driver)
    actual_elements.open_jn()
    actual_elements.login()
    actual_elements.click_and_open_company_tab()
    actual_elements.click_create_company_tab()
    actual_elements.assert_found_elements_on_add_company_page()


@allure.feature('')
@allure.severity('')
@allure.story('')
def test_create_heck_UNN(driver):
    """
    Стронний сервис по поиску УНП
    """
    create_company = Company(driver)
    create_company.open_jn()
    create_company.login()
    create_company.click_and_open_company_tab()
    create_company.click_create_company_tab()
    create_company.drop_city_selection()
    create_company.drop_locale_selection()
    create_company.drop_timezone_selection()
    create_company.drop_sell_strategy_selection()
    create_company.drop_registration_type_selection()
    create_company.drop_manager_selection()
    create_company.fill_fields_vat_number()
    create_company.click_save_company()
    create_company.assert_found_text_after_searching_vat_number()


@allure.feature('')
@allure.severity('')
@allure.story('')
def test_error_checking_max_number_of_characters(driver):
    """
    Проверка нотификаций по макс кол символов

    """
    create_company = Company(driver)
    create_company.open_jn()
    create_company.login()
    create_company.click_and_open_company_tab()
    create_company.click_create_company_tab()
    create_company.drop_city_selection()
    create_company.drop_locale_selection()
    create_company.drop_timezone_selection()
    create_company.drop_sell_strategy_selection()
    create_company.drop_registration_type_dropdown()
    create_company.drop_manager_selection()
    create_company.fill_fields_name_company()
    create_company.click_save_company()
    create_company.assert_found_errore_text()


@allure.feature('')
@allure.severity('')
@allure.story('')
def test_error_checking_min_number_of_characters(driver):
    """
    Проверка нотификаций по минимальному колличеству символов

    """
    create_company = Company(driver)
    create_company.open_jn()
    create_company.login()
    create_company.click_and_open_company_tab()
    create_company.click_create_company_tab()
    create_company.drop_city_selection()
    create_company.drop_locale_selection()
    create_company.drop_timezone_selection()
    create_company.drop_sell_strategy_selection()
    create_company.drop_registration_type_dropdown()
    create_company.drop_manager_selection()
    create_company.fill_fields_name_min_company()
    create_company.click_save_company()
    create_company.assert_found_errore_min_text()


@allure.feature('')
@allure.severity('')
@allure.story('')
def test_error_checking_UNN_number_of_characters(driver):
    """
    Проверка нотификаций УНП кол символов

    """
    create_company = Company(driver)
    create_company.open_jn()
    create_company.login()
    create_company.click_and_open_company_tab()
    create_company.click_create_company_tab()
    create_company.drop_city_selection()
    create_company.drop_locale_selection()
    create_company.drop_timezone_selection()
    create_company.drop_sell_strategy_selection()
    create_company.drop_registration_type_dropdown()
    create_company.drop_manager_selection()
    create_company.fill_fields_name_min_company()
    create_company.click_save_company()
    create_company.assert_found_errore_UNN_min_text()


@allure.feature('')
@allure.severity('')
@allure.story('')
def test_legal_name_validation_check(driver):
    """
    Проверка валидации легал имени
    """
    create_company = Company(driver)
    create_company.open_jn()
    create_company.login()
    create_company.click_and_open_company_tab()
    create_company.click_create_company_tab()
    create_company.drop_city_selection()
    create_company.drop_locale_selection()
    create_company.drop_timezone_selection()
    create_company.drop_sell_strategy_selection()
    create_company.drop_registration_type_dropdown()
    create_company.drop_manager_selection()
    create_company.fill_fields_legal_name()
    create_company.click_save_company()
    create_company.assert_found_errore_text_legal_name()


@allure.feature('')
@allure.severity('')
@allure.story('')
def test_required_fields_check(driver):
    """
    Проверка обязательных полей
    """
    create_company = Company(driver)
    create_company.open_jn()
    create_company.login()
    create_company.click_and_open_company_tab()
    create_company.click_create_company_tab()
    create_company.drop_city_selection()
    create_company.click_save_company()
    create_company.assert_required_fields()


@allure.feature('')
@allure.severity('')
@allure.story('')
def test_disable_fields_after_saving(driver):
    """
    Дизэйбл полей после сохранения компании
    """
    create_company = Company(driver)
    create_company.open_jn()
    create_company.login()
    create_company.click_and_open_company_tab()
    create_company.click_create_company_tab()
    create_company.drop_city_selection()
    create_company.drop_locale_selection()
    create_company.drop_timezone_selection()
    create_company.drop_sell_strategy_selection()
    create_company.drop_registration_type_dropdown()
    create_company.drop_manager_selection()
    create_company.fill_fields()
    create_company.click_save_company()
    create_company.assert_disable_elements_in_new_company()


@allure.feature('')
@allure.severity('')
@allure.story('')
def test_disable_elements_with_select_registration_type(driver):
    """
    Дизэйбл полей при выборе Registration type
    """
    create_company = Company(driver)
    create_company.open_jn()
    create_company.login()
    create_company.click_and_open_company_tab()
    create_company.click_create_company_tab()
    create_company.drop_sell_strategy_selection()
    create_company.drop_registration_type_dropdown()
    create_company.assert_disable_elements_with_select_registration_type()


@allure.feature('')
@allure.severity('')
@allure.story('')
def test_open_new_company_without_copay_1(driver):
    """
    Создание компании без copay и открытие для редактирования
    """
    create_company = Company(driver)
    create_company.open_jn()
    create_company.login()
    create_company.click_and_open_company_tab()
    create_company.click_create_company_tab()
    create_company.drop_city_selection()
    create_company.drop_locale_selection()
    create_company.drop_timezone_selection()
    create_company.drop_sell_strategy_selection()
    create_company.drop_registration_type_selection()
    create_company.drop_manager_selection()
    create_company.fill_fields()
    create_company.click_save_company()
    create_company.click_and_open_company_tab()
    create_company.open_last_dropdown_and_edit()
    create_company.assert_open_and_found_new_company()


def test_check_disable_elements_in_new_company_with_copay(driver):
    """
    Создание компании с copay и проверка через редактирование дизэйбл полей

    """
    create_company_with_copay = Company(driver)
    create_company_with_copay.open_jn()
    create_company_with_copay.login()
    create_company_with_copay.click_and_open_company_tab()
    create_company_with_copay.click_create_company_tab()
    create_company_with_copay.drop_city_selection()
    create_company_with_copay.drop_locale_selection()
    create_company_with_copay.drop_timezone_selection()
    create_company_with_copay.drop_sell_strategy_selection()
    create_company_with_copay.drop_registration_type_dropdown()
    create_company_with_copay.drop_manager_selection()
    create_company_with_copay.fill_fields()
    create_company_with_copay.click_save_company()
    create_company_with_copay.click_and_open_company_tab()
    create_company_with_copay.open_last_dropdown_and_edit()
    create_company_with_copay.assert_disable_elements_in_new_company()


def test_checking_filter_by_manager(driver):
    """
    Проверка фильтра по менеджеру

    """
    create_company_with_copay = Company(driver)
    create_company_with_copay.open_jn()
    create_company_with_copay.login()
    create_company_with_copay.click_and_open_company_tab()
    create_company_with_copay.drop_manager_selection_for_select()
    create_company_with_copay.assert_find_company_with_manager()


def test_checking_search_company(driver):
    """
    Проверка поиска компании

    """
    create_company_with_copay = Company(driver)
    create_company_with_copay.open_jn()
    create_company_with_copay.login()
    create_company_with_copay.click_and_open_company_tab()
    create_company_with_copay.search_field_company()
    create_company_with_copay.assert_find_company_search_field()


@allure.feature('')
@allure.severity('')
@allure.story('')
def test_create_new_and_delete_company(driver):
    """
    Создание компании без copay и удаление
    """
    create_company = Company(driver)
    create_company.open_jn()
    create_company.login()
    create_company.click_and_open_company_tab()
    create_company.click_create_company_tab()
    create_company.drop_city_selection()
    create_company.drop_locale_selection()
    create_company.drop_timezone_selection()
    create_company.drop_sell_strategy_selection()
    create_company.drop_registration_type_selection()
    create_company.drop_manager_selection()
    create_company.fill_fields()
    create_company.click_save_company()
    create_company.click_and_open_company_tab()
    create_company.delete_last_company()
    create_company.click_delete_company()
    create_company.assert_company_not_found()
