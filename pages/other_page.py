from pages.base_page import BasePage
from locators.other_locator import Other as other


class Others(BasePage):
    def catalog_data(self):
       self.element_is_present(other.ADMINIRIROVANIE).click()
       self.element_is_present(other.SELECT).click()
       self.element_is_present(other.CONTROL_DATA).click()
       self.element_is_present(other.SAVE).click()
    def message(self):
        self.element_is_present(other.MESSAGE).click()
        self.element_is_visible(other.ADD_MESSAGE).click()
        self.element_is_visible(other.USERS).click()
        self.element_is_visible(other.ADMIM).click()
        self.element_is_visible(other.USERS).click()
        self.element_is_visible(other.TITLE).send_keys("Тест 31.03.2023")
        self.element_is_visible(other.ROLES).click()
        self.element_is_visible(other.TEST_ROLE).click()
        self.element_is_visible(other.ROLES).click()
        self.element_is_visible(other.TEXT).send_keys("Текстовый текст")
        self.element_is_present(other.SITE).click()
        self.element_is_present(other.MAIL).click()
        self.element_is_visible(other.SAVE).click()




