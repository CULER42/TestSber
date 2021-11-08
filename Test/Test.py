
from pageObject.page_main import mainPage
from pageObject.page_translator import translatorPage
from selenium import webdriver
import pytest
import time



@pytest.mark.smoke
def test_yandex_translate(browser):
    pageMain = mainPage(browser)
    pageMain.go_to_site()
    time.sleep(2)
    assert pageMain.get_title() == 'Яндекс'
    assert pageMain.get_logo_yandex() is not None
    pageMain.link_yandex_translator()
    pageTranslator = translatorPage(browser)
    time.sleep(2)
    pageTranslator.switch_tab()
    assert pageTranslator.get_title() == 'Яндекс.Переводчик – словарь и онлайн перевод на английский, русский, немецкий, французский, украинский и другие языки.'
    assert pageTranslator.get_lang_button_translate() == 'АНГЛИЙСКИЙ'
    assert pageTranslator.get_lang_button_result_translation() == 'РУССКИЙ'
    pageTranslator.switch_laungage_arrows()
    assert pageTranslator.get_lang_button_translate() == 'РУССКИЙ'
    assert pageTranslator.get_lang_button_result_translation() == 'АНГЛИЙСКИЙ'
    pageTranslator.text_area_translate('Привет мир')
    time.sleep(2)
    assert pageTranslator.get_text_area_translation() == 'Hello world'





