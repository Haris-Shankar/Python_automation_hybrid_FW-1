import pytest
from selenium import webdriver
from utilities.logger import LogGen
import datetime



@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")

    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    else:
        driver = webdriver.Edge()

    return driver

def pytest_addoption(parser):  # This will get the value from cli
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#### It is hook for adding environment details  info to HTML report

def pytest_configure(config):
    # Adding custom environment details
    html_file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    html_path = f".//Reports/Reports_{html_file_name}.html"
    config.option.htmlpath = html_path

    logger = LogGen.loggen()
    if hasattr(config, "_metadata"):
        logger.info("Accessing _metadata and adding environment details.")
        config._metadata['Project Name'] = 'nop commerce'
        config._metadata['Module Name'] = 'Login'
        config._metadata['Tester'] = 'Your Name'
        config._metadata['Environment'] = 'QA'
    else:
        logger.error("_metadata not found")


def pytest_metadata(metadata):
    # Remove default metadata
    metadata.pop("Plugins", None)  # Remove Plugins information
    metadata.pop("Platform", None)  # Remove Platform information

