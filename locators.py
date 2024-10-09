REGISTER_BUTTON_XPATH = "//a[@class='Auth_link__1fOlj' and @href='/register']"  # Кнопка регистрации
NAME_FIELD_XPATH = "(//input[@class='text input__textfield text_type_main-default' and @type='text'])[1]"  # Поле ввода имени
EMAIL_FIELD_XPATH = "(//input[@class='text input__textfield text_type_main-default' and @type='text'])[2]"  # Поле ввода email
EMAIL_FIELD_LK_XPATH = "(//input[@class='text input__textfield text_type_main-default' and @type='text'])"
PASSWORD_FIELD_XPATH = "//input[@class='text input__textfield text_type_main-default' and @type='password']"  # Поле ввода пароля
SUBMIT_REGISTRATION_BUTTON_XPATH = "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Зарегистрироваться']"  # Кнопка подтверждения регистрации
REGISTRATION_LINK_XPATH = "//a[@class='Auth_link__1fOlj' and @href='/register']"
ERRORPASSWORD_MESSAGE_XPATH = "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']"  # Ошибка при некорректном пароле
LOGIN_BUTTON_XPATH = "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg' and text()='Войти в аккаунт']"
LOGIN_BUTTON_LK_XPATH = "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Войти']"
MAIN_LK_BUTTON = "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']"
LOGIN_LINK_LK = "//a[@class='Auth_link__1fOlj' and text()='Войти']"
PASSWORD_RECOVERY_LINK_XPATH = "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']"
CONSTRUCTOR_BUTTON_XPATH = "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']"
LOGO_CSS = "svg[xmlns='http://www.w3.org/2000/svg'][width='290'][height='50']"
LOGOUT_BUTTONLK_XPATH = "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive' and text()='Выход']"
ACTIVE_BUNS_TAB_XPATH = "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Булки']"
ACTIVE_SAUCES_TAB_XPATH = "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Соусы']"
SAUCES_TAB_XPATH = "//span[@class='text text_type_main-default' and text()='Соусы']"
ACTIVE_FILLINGS_TAB_XPATH = "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Начинки']"
FILLINGS_TAB_XPATH = "//span[@class='text text_type_main-default' and text()='Начинки']"