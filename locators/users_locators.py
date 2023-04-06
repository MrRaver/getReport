from selenium.webdriver.common.by import By

class Users:
    EDIT_ADDITIONAL = (By.XPATH, "/html/body/div/div/div[3]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div/div[2]/table/tbody/tr[5]/td/div/div/div[4]/a")  # настройки справочника таблицы
    THE_RIGHT=(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div/div[1]/ul/li[2]") #Права редактирование
    ADD_THE_RIGHT=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/table/thead/tr/th[7]/button")# добавить роль
    NAMES_ROLE=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/table/tbody/tr[2]/td[2]/div") #Названре роли
    NAMES_ROLE_ENTER=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/table/tbody/tr[2]/td[2]/div/div/div[1]/span") #поле ввода
    INPUT_NAMES_ROLE_ENTER=(By.XPATH,"/html/body/div[2]/input[1]") #поле ввода
    SEES=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/a") #Видит
    FIND_ELEMENT=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/div/div[1]/div[1]/div[3]/sb-multy-select/div/div/div[1]/div[2]") #Поиск элементов
    NUMBER_ID=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/div/div[1]/div[1]/div[3]/sb-multy-select/div/div/div[2]/div[2]/div[1]/div[3]") #Номер
    STRING=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/div/div[1]/div[1]/div[3]/sb-multy-select/div/div/div[2]/div[2]/div[1]/div[5]") #строка
    OK=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/div/div[1]/div[1]/div[3]/sb-multy-select/div/div/div[2]/div[2]/div[4]/button[1]")#ок, поиск элементов
    CHECKBOX_ALL_STATUS=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/div/div[1]/div[2]/div[1]/div/ins")#чек бокс все статусы
    ADD_FIELD=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/table/tbody/tr[2]/td[4]/div/div[1]/div[1]/div/ins") #добавляет чекбокс
    EDIT_FIELD = (By.XPATH, "/html/body/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/table/tbody/tr[2]/td[4]/div/div[2]/div[1]/div/ins") #редактирует поля и статусы чекбокс
    TRANSLITION_ALL_STATUS=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/table/tbody/tr[2]/td[5]/div/div[1]/div[1]/div/ins") #все статусы
    SAVE=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/div[2]/button") #Сохранить
    EDITS=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/table/tbody/tr[2]/td[4]/a") #столбие редактирует
    BUSINESS_PROCESS=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/table/tbody/tr[2]/td[5]/a") #столбик бизнес процессы
    DELETE_GR1=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/table/tbody/tr[2]/td[7]/button") #удалить gr1
    OKAY=(By.XPATH,"/html/body/div[1]/div/div/div/div[3]/button[1]") #Да удалить

    ROLES=(By.XPATH,"/html/body/div/div/div[2]/ul/li[3]")#Роли
    ADD_ROLE=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div/group-panel/panel/div/div[1]/panel-title/div[1]/a[2]") #создать роль
    ROLES_NAME=(By.XPATH,"/html/body/div[1]/div/div/group-edit-modal/modal-wnd/div[2]/body-block/div/div[1]/div/input") #вписать имя
    INPUT_ROLES_NAME=(By.XPATH,"/html/body/div[1]/div/div/group-edit-modal/modal-wnd/div[2]/body-block/div/div[1]/div/input")
    SAVE_ROLE=(By.XPATH,"/html/body/div[1]/div/div/group-edit-modal/modal-wnd/div[3]/ul/li[2]/button")#сохранить роль

    USERS=(By.XPATH,"/html/body/div/div/div[2]/ul/li[2]")#Пользователи
    ADD_USERS=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/div[2]/a") #Добавить пользователя
    LOGIN_USER=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[2]/body-block/panel/div/div[2]/panel-body/account-edit-form/div/div/div[1]/div/div[2]/account-data/form/div[1]/div/input")#Логин
    EMAIL_USER=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[2]/body-block/panel/div/div[2]/panel-body/account-edit-form/div/div/div[1]/div/div[2]/account-data/form/div[2]/div/input")#Логин
    TABEL_NUMBER_USER=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[2]/body-block/panel/div/div[2]/panel-body/account-edit-form/div/div/div[1]/div/div[2]/account-data/form/div[3]/div/input")#Табельный номер
    LASTNAME_USER=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[2]/body-block/panel/div/div[2]/panel-body/account-edit-form/div/div/div[1]/div/div[2]/account-data/form/div[4]/div/input")# Фамилия
    FIRSTNAME_USER=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[2]/body-block/panel/div/div[2]/panel-body/account-edit-form/div/div/div[1]/div/div[2]/account-data/form/div[5]/div/input")# имя
    SURNAME_USER=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[2]/body-block/panel/div/div[2]/panel-body/account-edit-form/div/div/div[1]/div/div[2]/account-data/form/div[6]/div/input")# Фамилия
    PASSWORD_USER=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[2]/body-block/panel/div/div[2]/panel-body/account-edit-form/div/div/div[1]/div/div[2]/account-data/form/div[8]/div/input")# Пароль первая строка
    PASSWORD_USER2=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[2]/body-block/panel/div/div[2]/panel-body/account-edit-form/div/div/div[1]/div/div[2]/account-data/form/div[9]/div/input")# Пароль вторая строка
    USERS_ROLES=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[2]/body-block/panel/div/div[2]/panel-body/account-edit-form/div/div/div[2]/div/div[2]/roles-selector/div/div/button") #роли учетной записи
    SAVE_USERS=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[3]/ul/li[2]/button") #Сохранить пользователя
    REGISTRATION_EMAIL=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[2]/body-block/panel/div/div[1]/panel-title/ul/li[2]/a")#Регистрация по почте
    ADD_EMAIL_USERS=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[2]/body-block/panel/div/div[2]/panel-body/email-registration-form/table/thead/tr/th[3]/button")#добавить пользователя по почте
    EMAIL_BY_REGISTRATION=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[2]/body-block/panel/div/div[2]/panel-body/email-registration-form/table/tbody/tr/td[1]/textarea") #Ввод почты
    CHOICE_ROLE=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[2]/body-block/panel/div/div[2]/panel-body/email-registration-form/table/tbody/tr/td[2]/roles-selector/div/div/button") #Выбор ролей
    INPUT_CHOICE_ROLE=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[2]/body-block/panel/div/div[2]/panel-body/email-registration-form/table/tbody/tr/td[2]/roles-selector/div/div/ul/li[4]/div/input") #Выбор ролей
    CHOICES_ROLES=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[2]/body-block/panel/div/div[2]/panel-body/email-registration-form/table/tbody/tr/td[2]/roles-selector/div/div/ul/li[6]/a") #выбираем роль
    SAVE_EMAIL=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[3]/ul/li[2]/button")#Сохранение пользователя по почте

    REGISTRATION_BY_URL=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[2]/body-block/panel/div/div[1]/panel-title/ul/li[3]/a")  #Регистрация по ссылке
    ADD_LINK_URL=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[2]/body-block/panel/div/div[2]/panel-body/link-registration-form/table/thead/tr/th[4]/button") #Добавить
    CHOICE_URL=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[2]/body-block/panel/div/div[2]/panel-body/link-registration-form/table/tbody/tr/td[3]/roles-selector/div/div/button")
    INPUT_CHOICE_URL=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[2]/body-block/panel/div/div[2]/panel-body/link-registration-form/table/tbody/tr/td[3]/roles-selector/div/div/ul/li[4]/div/input")
    CHOICES_URL=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[2]/body-block/panel/div/div[2]/panel-body/link-registration-form/table/tbody/tr/td[3]/roles-selector/div/div/ul/li[6]/a")
    SAVE_URL_LINK=(By.XPATH,"/html/body/div[1]/div/div/registration-modal/modal-wnd/div[3]/ul/li[2]/button")

    ADD_USERS_IN_ROLES=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/panel/div/div[2]/panel-body/user-panel/panel/div/div[1]/panel-title/div[1]/a") #Добавить вложенного пользователя
    CHOICE_ELEMENT=(By.XPATH,"/html/body/div[1]/div/div/group-select-modal/modal-wnd/div[2]/body-block/div/div/div/group-select/table/tbody/tr/td/div/div/button") #Выберите элемент
    INPUT_INUSERS=(By.XPATH,"/html/body/div[1]/div/div/group-select-modal/modal-wnd/div[2]/body-block/div/div/div/group-select/table/tbody/tr/td/div/div/ul/li[4]/div/input") #Вписать имя
    CHOICE_FIRST_VARIANT=(By.XPATH,"/html/body/div[1]/div/div/group-select-modal/modal-wnd/div[2]/body-block/div/div/div/group-select/table/tbody/tr/td/div/div/ul/li[6]/a")
    SAVE_INUSERS=(By.XPATH,"/html/body/div[1]/div/div/group-select-modal/modal-wnd/div[3]/ul/li[2]/button") #Сохранить вложенного пользователя
    TEST_ROLE_GR1=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[3]/div/group-panel/panel/div/div[2]/panel-body/group-list/ul/li[3]") #Тестовая роль GR1

    OFF_URL=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[2]/div/div/div/div[2]/custom-grid-simple/custom-grid/div[1]/div[2]/table/tbody/tr[6]/td[8]/ng-html-include/div") #Выключаем приглашенный по ссылке
    TEXT_ERROR=(By.XPATH,"/html/body/div[1]/div/div/alert-modal/div/alert-slider/table/tbody/tr/td[2]/p[1]") #Текст ошибки
    ENTER_BY_URL=(By.XPATH,"/html/body/div/div/div[3]/div/div/div/div[2]/div/div/div/div[2]/custom-grid-simple/custom-grid/div[1]/div[2]/table/tbody/tr[6]/td[9]/ng-html-include/button") #Войти













