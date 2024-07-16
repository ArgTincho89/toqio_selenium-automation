import pytest
import logging
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from utilities.test_data import TestData

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

@pytest.fixture(params=["chrome",  "firefox", "edge"
                        ])
def initialize_driver(request):
    if request.param == "chrome":
        chrome_options = ChromeOptions()
        # chrome_options.add_argument("--start-maximized") # Enable this option only while running in headed mode
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == "firefox":
        firefox_options = FirefoxOptions()
        #firefox_options.set_preference("fullScreen", True)
        firefox_options.set_preference("window.size.width", 1920)
        firefox_options.set_preference("window.size.height", 1080)  
        firefox_options.add_argument("-private")
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Firefox(options=firefox_options)
    elif request.param == "edge":
        edge_options = EdgeOptions()
        #edge_options.add_argument("--start-maximized")
        edge_options.add_argument("--window-size=1920,1080")
        edge_options.add_argument("--inprivate")
        edge_options.add_argument("--headless")
        edge_options.add_argument("--no-sandbox")
        edge_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Edge(options=edge_options)

    request.cls.driver = driver
    print("Browser: ", request.param)
    driver.get(TestData.url)

    yield driver
    print("Close Driver")
    driver.quit()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        extra.append(pytest_html.extras.url('https://toqio.co/'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
            if report.failed:
                driver = getattr(item, 'cls', None).driver
                failures_dir = os.path.join("..", "reports", "failures")
                if not os.path.exists(failures_dir):
                    os.makedirs(failures_dir)
                file_name = os.path.join(failures_dir, report.nodeid.replace("::", "_").replace("/", "_") + ".png")
                driver.save_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
        report.extra = extra