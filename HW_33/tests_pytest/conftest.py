import time

import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
options = Options()
# options.add_argument("start-maximized"); # open Browser in maximized mode
options.add_argument("--no-sandbox")

test_config = 'test.prop'
prod_config = 'prod.prop'

@pytest.fixture()
def set_up_page(set_up_context, browser):
    # context = browser.new_context(storage_state='state.json')
    context = set_up_context
    page = context.new_page()
    page.goto("https://demoqa.com/profile")  # Go to https://www.wikipedia.org/
    page.wait_for_load_state()
    yield page
    page.close()

@pytest.fixture()
def set_up_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://bstackdemo.com/")
    yield driver
    driver.quit()


@pytest.fixture
def set_up1(browser) -> None:
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)  # slow_mo wait for every action
    context = browser.new_context()

    # Open new page
    page = context.new_page()
    # home_page = Home(page)
    page.goto("https://www.wikipedia.org/")  # Go to https://www.wikipedia.org/
    page.wait_for_load_state()
    yield page


def pytest_addoption(parser):
    parser.addoption('--cmdopt', default='Test')


@pytest.fixture
def command_param(pytestconfig):
    opt = pytestconfig.getoption('cmdopt')
    if opt == 'Test':
        f = open(os.path.join(os.path.dirname(__file__), test_config), 'r')
    else:
        f = open(os.path.join(os.path.dirname(__file__), prod_config), 'r')
    yield f


def pytest_configure():
    pytest.cites = ['fdsfsd', 'fdsfsd23', 'fdsf1']

# @pytest.fixture(scope='module')
@pytest.fixture()
def setup_list_import():
    pycities = pytest.cites.copy()
    pycities.append('tretret')
    yield pycities
    print('After fixture')


# @pytest.fixture(scope="session")
@pytest.fixture()
def setup_list_import_factory():
    def get_structure():
        pycities = pytest.cites.copy()
        pycities.append('tretret')
        return pycities

    return get_structure


@pytest.fixture()
def setup_list_import2():
    pycities = pytest.cites.copy()
    pycities.append('tretret2')
    yield pycities
    print('After fixture2')


@pytest.fixture()
def setup_list_import3(request):
    month = getattr(request.module, 'month')
    print('\n Fixture3 Scope: ' + str(request.scope))
    print('\n Calling setup_list_import3: ' + str(request.function.__name__) + ' \n')
    print('\n Calling setup_list_import3 in module: ' + str(request.module.__name__) + ' \n')
    month.append('april')
    yield month


@pytest.fixture()
def factory_fixture():
    def get_structure(name):
        if name == 'list':
            return [1, 2, 3]
        elif name == 'tuple':
            return (1, 2, 3)

    return get_structure


@pytest.fixture(params=[(3, 4), [3, 5]], ids=['tuple', 'list'])
def params_fixture(request):
    return request.param


@pytest.fixture(params=['access', 'slice'])
def params_fixture2(request):
    return request.param
