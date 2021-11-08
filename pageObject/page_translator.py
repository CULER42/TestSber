
from BaseApp.BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class translatorPageLocators:
    locator_switch_language= (By.XPATH,"//button[@aria-label='Переключить направление']")
    locator_lang_button_translate = (By.ID, "srcLangButton")
    locator_lang_button_result_translation = (By.ID,'dstLangButton')
    locator_text_area_translate = (By.ID,'fakeArea')
    locator_text_translation = (By.ID,'translation')



class translatorPage(BasePage):

     def switch_laungage_arrows(self):
         switchLaungageArrows = self.find_element(translatorPageLocators.locator_switch_language)
         return switchLaungageArrows.click()

     def get_lang_button_translate(self):
         getLangButtonTranslate = self.find_element(translatorPageLocators.locator_lang_button_translate)
         getLangButton = getLangButtonTranslate.text
         return getLangButton

     def get_lang_button_result_translation(self):
         getLangButtonResultTranslation = self.find_element(translatorPageLocators.locator_lang_button_result_translation)
         getLangButtonResult = getLangButtonResultTranslation.text
         return getLangButtonResult

     def text_area_translate(self,word):
         textAreaTranslate = self.find_element(translatorPageLocators.locator_text_area_translate)
         textAreaTranslate.send_keys(word)
         textAreaTranslate.send_keys(Keys.ENTER)
         return textAreaTranslate


     def get_text_area_translation(self):
         getTextAreaTranslation = self.find_element(translatorPageLocators.locator_text_translation)
         getTextArea = getTextAreaTranslation.text
         return getTextArea





