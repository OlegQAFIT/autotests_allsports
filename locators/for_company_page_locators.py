class CompanyPageLocators():
    FOOTER_COMPANY = "//a[text()='Companies']"

    CREATE_COMPANY = "//button[contains(@class, 'btn-primary') and contains(., 'Create Company')]"

    LOCATION_DROP_DOWN = '//*[@class="select-input_label" and text()=" Location: "]/following-sibling::div/select'
    MINSK_VALUE = '//option[@value="Minsk"]'
    MOGILEV_VALUE = "//select[@class='']/option[@value='Mogilev']"
    BREST_VALUE = "//select[@class='']/option[@value='Brest']"
    GRODNO_VALUE = "//select[@class='']/option[@value='Grodno']"
    GOMEL_VALUE = "//select[@class='']/option[@value='Gomel']"
    VITEBSK_VALUE = "//select[@class='']/option[@value='Vitebsk']"

    LOCALE_DROP_DOWN = '//*[@class="select-input_label" and text()=" Locale: "]/following-sibling::div/select'
    AM_VALUE = "//select[@class='']/option[@value='am']"
    EN_VALUE = "//select[@class='']/option[@value='en']"
    EN_LT_VALUE = "//select[@class='']/option[@value='en_LT']"
    LT_LT_VALUE = "//select[@class='']/option[@value='lt_LT']"
    RU_VALUE = '//option[@value="ru"]'
    UK_VALUE = "//select[@class='']/option[@value='uk']"

    TIMEZONE_DROP_DOWN = "/html/body/div/div/div[2]/form/section[1]/div[1]/label/div/input"
    MINSK_VALUE_TIMEZONE = "/html/body/div/div/div[2]/form/section[1]/div[1]/ul/li[349]/a"

    SELL_STRATEGY_DROP_DOWN = '//*[@class="select-input_label" and text()=" Sell Strategy "]/following-sibling::div/select'
    COUNTRY_VALUE = '//option[@value="country"]'
    BY1_VALUE = "//select[@class='']/option[@value='by1']"
    BY2_VALUE = "//select[@class='']/option[@value='by2']"

    REGISTRATION_TYPE_STANDARD = "//select[@class='']/option[@value='0']"
    REGISTRATION_TYPE_FORM = "//select[@class='']/option[@value='1']"

    dropdown = "/html/body/div/div/div[2]/form/section[1]/div[2]/label/div/select"

    default_subscription = "/html/body/div/div/div[2]/form/section[1]/div[2]/label[2]/div/select"

    compensation_type = "/html/body/div/div/div[2]/form/section[1]/div[2]/label[3]/div/select"

    ID = "/html/body/div/div/div[2]/form/section[1]/label[1]/div/input"
    compensation_amount = "/html/body/div/div/div[2]/form/section[1]/div[2]/label[4]/div/input"

    COMPANY_INPUT = "/html/body/div/div/div[2]/form/section[1]/label[5]/div/input"

    MANAGER_DROP_DOWN = "//label[@class='select-input large']//select[@class='quiet']"
    MANAGER_FILIP_WOLEK = "//select[@class='quiet']/option[@value='2']"
    MANAGER_AUTOTEST_ADMIN_FILIP = "//select[@class='quiet']/option[@value='18']"
    MANAGER_AUTOTEST_ADMIN_ALEX = "//select[@class='quiet']/option[@value='19']"
    MANAGER_NADEZHDA_SADOVSKAYA = "//select[@class='quiet']/option[@value='231']"
    MANAGER_SUPPORT = "//select[@class='quiet']/option[@value='238']"
    MANAGER_AUTOTEST_ALVINA_MCDERMOTT_II = "//select[@class='quiet']/option[@value='245']"
    MANAGER_AUTOTEST_GRANVILLE_GREENHOLT = "//select[@class='quiet']/option[@value='246']"
    MANAGER_QA_YULIA_B = "//select[@class='quiet']/option[@value='252']"
    MANAGER_QA_BAKURIN_A = "//select[@class='quiet']/option[@value='253']"
    MANAGER_QA_RYZHKO_A = "//select[@class='quiet']/option[@value='254']"
    MANAGER_QA_KAHADOUSKAYA_N = "//select[@class='quiet']/option[@value='255']"
    MANAGER_QA_NOVOGRAN_V = "//select[@class='quiet']/option[@value='256']"
    MANAGER_QA_PAVEL_L = "//select[@class='quiet']/option[@value='258']"
    MANAGER_QA_YAN_S = "//select[@class='quiet']/option[@value='259']"
    MANAGER_QA_ANDREY_L = "//select[@class='quiet']/option[@value='260']"
    MANAGER_QA_DARIA_S = "//select[@class='quiet']/option[@value='261']"
    MANAGER_QA_OLEG_A = "//select[@class='quiet']/option[@value='262']"
    MANAGER_TEST1 = "//select[@class='quiet']/option[@value='265']"
    MANAGER_ALEX_DEV_TEST = "//select[@class='quiet']/option[@value='269']"
    MANAGER_ALEX = "//select[@class='quiet']/option[@value='270']"

    DATE = "/html/body/div/div/div[2]/form/section[2]/label[1]/div/input"
    DATE_INPUT = "(//div[@data-v-3e74a67c]//input[@type='text'])[1]"
    DATE_TEXT = "0130"

    MIN_ORDER_ITEMS = "//input[@data-v-8a5e45de and @type='text' and @disabled='disabled']"
    MIN_ORDER_ITEMS_INPUT = "/html/body/div/div/div[2]/form/section[2]/label[2]/div/input"

    VAT_NUMBER_INPUT = "//section[@class='section']//label[@class='large']/p[contains(text(),'VAT NUMBER')]/following" \
                       "-sibling::div/input[@type='text']"
    VAT_NUMBER_TEXT = "193190172"

    LEGAL_NAME_INPUT = "//label[@class='large' and p[@class='input_title' and contains(text(), 'Legal Name')]]//input[@type='text']"

    LEGAL_ADDRESS_INPUT = "//section[@class='section']//label[@class='large']/p[contains(text(),'Legal Address')]" \
                          "/following-sibling::div/input[@type='text']"
    LEGAL_ADDRESS_TEXT = "220030 г. Минск, ул. Интернациональная, 36-2, офисы 2-20, 1-21"

    CONTACT_PHONE_INPUT = "//section[@class='section']//label[@class='large']/p[contains(text(),'Contact Phone')]" \
                          "/following-sibling::div/input[@type='text']"
    CONTACT_PHONE_TEXT = "+375 (44) 502-36-13"

    MAX_COMPANY_NAME_TEXT = "222838, Республика Беларусь, Минская область, Пуховичский р-н, Новосёлковский с/с, д. 35, " \
                            "район улицы Зорный Шлях г. Марьина Горка Почтовый адрес: 220089, Республика Беларусь, г. " \
                            "Минск, ул. Железнодорожная, д. 33222838, Республика Беларусь, Минская область, Пуховичский" \
                            " р-н, Новосёлковский с/с, д. 35, район улицы Зорный Шлях г. Марьина Горка Почтовый адрес: " \
                            "220089, Республика Беларусь, г. Минск, ул. Железнодорожная, д. 33"

    ERRORE_TEXT = "//div[@class='info-banner info-banner__visible']//p[@class='info-banner_message' and @data-v-32f372a4]"

    ERRORE_TEXT_legal_name = "/html/body/div/div/div[2]/form/section[3]/label[2]/div/span"

    ERRORE_TEXT_LEGAL_NAME = "//span[@data-v-8a5e45de and @data-error-type='message' and contains(text(), 'Такое значение поля legal name уже существует.')]"


    SWIFT_INPUT = "//section[@class='section']//label[@class='large']/p[contains(text(),'SWIFT')]/following-sibling::" \
                  "div/input[@type='text']"

    ACCOUNT_INPUT = "//section[@class='section']//label[@class='large']/p[contains(text(),'Account')]/following-" \
                    "sibling::div/input[@type='text']"

    SAVE_AND_CONTINUE_BUTTON = "//button[contains(@class,'btn') and contains(.,'Save and continue')]"



    ADD_COMPANY = "/html/body/div/div/div[2]/form/div[1]/h1"
    HR_SETTINGS = "/html/body/div/div/div[2]/form/h2[1]"
    DATA_FOR_THE_CONTRACT = "/html/body/div/div/div[2]/form/h2[2]"
    BENEFIARY = "/html/body/div/div/div[2]/form/h2[3]"
    OPTIONAL = "/html/body/div/div/div[2]/form/h2[4]"

    LEGAL_NAME_SEARCH = "/html/body/div/div/div[2]/form/section[3]/label[2]/div"

    Locale_required_fields = "/html/body/div/div/div[2]/form/section[1]/label[2]/div/span"
    Timezone_required_fields = "/html/body/div/div/div[2]/form/section[1]/div[1]/div"
    Sell_Strategy_required_fields = "/html/body/div/div/div[2]/form/section[1]/label[3]/div/span"
    Company_Name_required_fields = "/html/body/div/div/div[2]/form/section[1]/label[5]/div/span"
    VAT_NUMBER_required_fields = "/html/body/div/div/div[2]/form/section[3]/label[1]/div/span"
    Legal_Name_required_fields = "/html/body/div/div/div[2]/form/section[3]/label[2]/div/span"
    Legal_Address_required_fields = "/html/body/div/div/div[2]/form/section[4]/label[1]/div/span"
    Contact_Phone_required_fields = "/html/body/div/div/div[2]/form/section[4]/label[2]/div/span"