import logging

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey
# import appium.webdriver.extensions.android.nativekey as nativekey
from selenium.webdriver import Keys

from Utilities.LogUtil import Logger
from Utilities import configReader

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # def click(self, locator):
    #     if str(locator).endswith("_XPATH"):
    #         self.driver.find_element_by_xpath(configReader.readConfig("locators", locator)).click()
    #     elif str(locator).endswith("_ACCESSIBILITYID"):
    #         self.driver.find_element_by_accessibility_id(configReader.readConfig("locators", locator)).click()
    #     elif str(locator).endswith("_ID"):
    #         self.driver.find_element_by_id(configReader.readConfig("locators", locator)).click()
    #     log.logger.info("Clicking on an Element "+ str(locator))

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(by=AppiumBy.XPATH, value=configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,
                                     value=configReader.readConfig("locators", locator)).click()
            # self.driver.find_element_by_accessibility_id(configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            self.driver.find_element(by=AppiumBy.ID, value=configReader.readConfig("locators", locator)).click()
            # self.driver.find_element_by_id(configReader.readConfig("locators", locator))
        log.logger.info("Clicking on an Element " + str(locator))

    def clickIndex(self, locator, index):
        if str(locator).endswith("_XPATH"):
            self.driver.find_elements(by=AppiumBy.XPATH, value=configReader.readConfig("locators", locator))[index].click()
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_elements(by=AppiumBy.ACCESSIBILITY_ID, value=configReader.readConfig("locators", locator))[index].click()
        elif str(locator).endswith("_ID"):
            self.driver.find_elements(by=AppiumBy.ID, value=configReader.readConfig("locators", locator))[index].click()
        log.logger.info("Clicking on an Element " + str(locator) + "with index : " + str(index))

    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(by=AppiumBy.XPATH, value=configReader.readConfig("locators", locator)).send_keys(
                value)
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,
                                     value=configReader.readConfig("locators", locator)).send_keys(value)
            # self.driver.find_element_by_accessibility_id(configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            self.driver.find_element(by=AppiumBy.ID, value=configReader.readConfig("locators", locator)).send_keys(
                value)
        elif str(locator).endswith("_CLASSNAME"):
            self.driver.find_element(by=AppiumBy.CLASS_NAME, value=configReader.readConfig("locators", locator)).send_keys(
                value)
        log.logger.info("Typing in an Element " + str(locator) + " entered the value as : " + str(value))

    def getText(self, locator):
        self.driver.implicitly_wait(20)
        text = None
        if str(locator).endswith("_XPATH"):
            text = self.driver.find_element(by=AppiumBy.XPATH, value=configReader.readConfig("locators", locator)).text
        elif str(locator).endswith("_ACCESSIBILITYID"):
            text = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=configReader.readConfig("locators", locator)).text
        elif str(locator).endswith("_ID"):
            text = self.driver.find_element(by=AppiumBy.ID, value=configReader.readConfig("locators", locator)).text
        #log.logger.info
        self.driver.implicitly_wait(10)
        return text

    def getTextIndex(self, locator, index):
        self.driver.implicitly_wait(20)
        text = None
        if str(locator).endswith("_XPATH"):
            text = self.driver.find_elements(by=AppiumBy.XPATH, value=configReader.readConfig("locators", locator))[index].text
        elif str(locator).endswith("_ACCESSIBILITYID"):
            text = self.driver.find_elements(by=AppiumBy.ACCESSIBILITY_ID, value=configReader.readConfig("locators", locator))[index].text
        elif str(locator).endswith("_ID"):
            text = self.driver.find_elements(by=AppiumBy.ID, value=configReader.readConfig("locators", locator))[index].text
        log.logger.info("Clicking on an Element " + str(locator) + "with index : " + str(index))
        self.driver.implicitly_wait(10)
        return text

    def enter(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(by=AppiumBy.XPATH, value=configReader.readConfig("locators", locator)).send_keys(
                Keys.ENTER)
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,
                                     value=configReader.readConfig("locators", locator)).send_keys(Keys.ENTER)
            # self.driver.find_element_by_accessibility_id(configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            self.driver.find_element(by=AppiumBy.ID, value=configReader.readConfig("locators", locator)).send_keys(
                Keys.ENTER)
        log.logger.info("Typing in an Element " + str(locator) + " entered the value as : " + str(Keys.ENTER))

    def pressEnter(self):
        self.driver.keyevent(AndroidKey.ENTER)
        log.logger.info("Hit enter button the value as : " + str(AndroidKey.ENTER))

    def insertMobileNo(self):
        self.driver.keyevent(AndroidKey.DIGIT_9)
        log.logger.info("Hit enter button the value as : " + str(AndroidKey.DIGIT_9))
        self.driver.keyevent(AndroidKey.DIGIT_7)
        log.logger.info("Hit enter button the value as : " + str(AndroidKey.DIGIT_7))
        self.driver.keyevent(AndroidKey.DIGIT_5)
        log.logger.info("Hit enter button the value as : " + str(AndroidKey.DIGIT_5))
        self.driver.keyevent(AndroidKey.DIGIT_4)
        log.logger.info("Hit enter button the value as : " + str(AndroidKey.DIGIT_4))
        self.driver.keyevent(AndroidKey.DIGIT_4)
        log.logger.info("Hit enter button the value as : " + str(AndroidKey.DIGIT_4))
        self.driver.keyevent(AndroidKey.DIGIT_2)
        log.logger.info("Hit enter button the value as : " + str(AndroidKey.DIGIT_2))
        self.driver.keyevent(AndroidKey.DIGIT_3)
        log.logger.info("Hit enter button the value as : " + str(AndroidKey.DIGIT_3))
        self.driver.keyevent(AndroidKey.DIGIT_9)
        log.logger.info("Hit enter button the value as : " + str(AndroidKey.DIGIT_9))
        self.driver.keyevent(AndroidKey.DIGIT_9)
        log.logger.info("Hit enter button the value as : " + str(AndroidKey.DIGIT_9))
        self.driver.keyevent(AndroidKey.DIGIT_8)
        log.logger.info("Hit enter button the value as : " + str(AndroidKey.DIGIT_8))

    def pressBack(self):
        self.driver.keyevent(AndroidKey.BACK)
        log.logger.info("Hit back button the value as : " + str(AndroidKey.BACK))

    def switchActivity(self):
        # Switch to the Message app
        self.driver.startActivity('com.google.android.apps.messaging', '.ui.ConversationListActivity')

    def getElementCount(self, locator):
        global elements
        if str(locator).endswith("_XPATH"):
            elements = self.driver.find_elements(by=AppiumBy.XPATH, value=configReader.readConfig("locators", locator))
        return elements

