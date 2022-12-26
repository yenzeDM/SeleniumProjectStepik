import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: --language=Your language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    r_browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")

        options = ChromeOptions()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})

        path = Service(ChromeDriverManager().install())

        r_browser = webdriver.Chrome(service=path, options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")

        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)

        path = None

        r_browser = webdriver.Firefox(executable_path=path, options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield r_browser
    print("\nquit browser..")
    r_browser.quit()
