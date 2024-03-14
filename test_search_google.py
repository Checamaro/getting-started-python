import pytest
from selene import browser, have, be
from selene.support.shared import browser
from selene.support.shared import browser as shared_browser

"""Открываем браузер Chrome и страницу поиска Google"""


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.driver_name = 'chrome'
    shared_browser.driver.maximize_window()
    browser.config.base_url = 'https://google.com'


"""В строке поиска вводим слово 'python' """


def test_search_python():
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type('afdvceargqeq354e62cerg6r4g16vwer4geq').press_enter()
    browser.element('[id="botstuff"]').should(have.text('Your search - afdvceargqeq354e62cerg6r4g16vwer4geq - did not match any documents.'))
