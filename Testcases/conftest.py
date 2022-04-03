from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        driver.maximize_window()
        print("launching chrome browser")
    else:
        driver=webdriver.Ie()
        print("launching IE browser")
    return driver
def pytest_addoption(parser):        #this will get the value fom CLI/hook
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
#pytest html repor:

#it is hook for adding Environment info to HTML reports:
def pytest_configure(config):
    config._metadata['Project Name']='nop commerce'
    config._metadata['Module Name']='Customer'
    config._metadata['Tester']='Vishnu'


#it is hook for delete or modify Environment info to HTML reports:
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME",None)
    metadata.pop("Pluggins",None)