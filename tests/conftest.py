import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
driver = None


def pytest_addoption(parser):
    """Create custom  CLI options to select  browser and environment where the test case will be performed """
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--environment_name", action="store", default="prod"
    )

@pytest.fixture(scope="class")
def setup(request):
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors-spki-list')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--start-maximized')
    """Setup the browser, the URL and the environment where the test case will be performed """
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="utilities/chromedriver.exe", options=chrome_options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="utilities/geckodriver.exe")
    environment_name = request.config.getoption("environment_name")
    if environment_name == "prod":
        driver.get("https://www.liverpool.com.mx/tienda/home")
    elif environment_name == "stg":
        driver.get("https://www.amazon.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """"
    Generate html report name with detail based on the time it was ran.
    """
    config.option.htmlpath = (
        "reports/" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
    )

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" or report.when == "setup":

        xfail = hasattr(report, "wasxfail")

        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = "reports/" + report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = (
                        '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                )
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)