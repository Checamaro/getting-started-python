import pytest
from selene import browser, have, be
from selene.support.shared import browser
from selene.support.shared import browser as shared_browser

"""Открываем браузер Chrome и страницу поиска Yandex"""


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.driver_name = 'chrome'
    browser.config.base_url = 'https://ya.ru'


"""В строке поиска вводим слово 'python' """


def test_search_python():
    browser.open('/')
    shared_browser.driver.maximize_window()
    browser.element('[name="text"]').should(be.blank).type('python').press_enter()
    # Проверяем, что в URL открывшейся страницы есть слово 'python'
    current_url = browser.driver.current_url
    assert 'python' in current_url.lower(), f"Word 'python' not found in URL: {current_url}"
