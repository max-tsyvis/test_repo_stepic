import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="eng",
                     help="Choose browser language")


@pytest.fixture(scope="function")
def browser(request):
    custom_options = Options()
    language = request.config.getoption("language")
    custom_options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=custom_options)
    print("open browser with language=",language)
    yield browser
    print("\nquit browser..")
    browser.quit()
