from BaseApp.BaseApp import BasePage
from selenium.webdriver.common.by import By


class mainPageLocators:
      locator_logo_yandex = (By.XPATH,'//div[@aria-label="Яндекс"]')
      locator_link_translator = (By.XPATH,'//a[@data-id="translate"]')



class mainPage(BasePage):

    def get_logo_yandex(self):
        logoYandex = self.find_element(mainPageLocators.locator_logo_yandex)
        return logoYandex


    def link_yandex_translator(self):
        linkYandex = self.find_element(mainPageLocators.locator_link_translator)
        return linkYandex.click()







