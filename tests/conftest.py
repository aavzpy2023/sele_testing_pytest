# General imports
import pytest
from selenium import webdriver

# Imports to get chrome driver working
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Imports to get firefox driver working
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Imports to get edge driver working
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager

# Import options for headless mode
from selenium.webdriver.chrome.options import Options as Go_Options
from selenium.webdriver.firefox.options import Options as Fx_Options
from selenium.webdriver.edge.options import Options as Ed_Options




def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="edge", help="Send 'edge' or 'chrome' or 'firefox' as parameter for execution"
    )
    parser.addoption(
        "--headless", action="store", default="", help="Send 'ok' to use headless or leave in blank for not use it as parameter for execution"   
    )


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    # Default driver value
    driver = ""
    
    # Setup
    print(f"\nSetting up: {browser} driver")
    if browser == "chrome":
        options = Go_Options()
        # Option setup to run in headless mode (in order to run this in GH Actions)
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser == "firefox":
        print(headless)
        options = Fx_Options()
        # Option setup to run in headless mode (in order to run this in GH Actions)
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    elif browser == "edge":
        options = Ed_Options()
        # Option setup to run in headless mode (in order to run this in GH Actions)
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    driver.implicitly_wait(30)
    yield driver
    # Tear down
    print(f"\nCLosing {browser} driver")
    driver.quit()

