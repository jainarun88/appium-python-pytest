import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.common import AppiumOptions


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def appium_driver(request):
    desired_caps = {
        'platformName': 'Android',
        # "deviceName": "96c5ce34",
        "automationName": "UIAutomator2",
        'appPackage': 'com.flipkart.android',
        'appActivity': 'com.flipkart.android.SplashActivity',
        # 'appPackage': 'com.google.android.apps.messaging',
        # 'appActivity': 'com.ui.ConversationListActivity',
        'noReset': True
    }

    url = "http://localhost:4723"

    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(caps=desired_caps))

    # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=AppiumOptions().load_capabilities(caps=desired_caps))
    request.cls.driver = driver
    driver.implicitly_wait(30)
    yield driver
    driver.quit()


@pytest.fixture()
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
