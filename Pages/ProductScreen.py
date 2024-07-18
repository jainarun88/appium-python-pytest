import logging
import re
from time import sleep

from Pages.BasePage import BasePage

from Utilities import configReader
from Utilities.LogUtil import Logger
from Utilities.scroll_util import ScrollUtil

log = Logger(__name__, logging.INFO)


class ProductScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def searchHotel(self, city):
        self.click("destination_ACCESSIBILITYID")
        self.type("searchtext_ID", city)
        self.clickIndex("selectlocation_ID", 0)
        self.click("searchbtn_XPATH")

    def navigateToSearchScreen(self):
        self.click("english_lan_XPATH")
        self.click("continue_btn_ID")
        self.click("skip_btn_ID")

    def searchForProduct(self, product_name):
        self.click("search_textbox_XPATH")
        self.type("search_text_2_CLASSNAME", product_name)
        self.pressEnter()

    def closeNotificationPopup(self):
        self.click("notification_not_now_XPATH")

    def closeLocationPopup(self):
        self.click("location_not_now_XPATH")

    def selectProduct(self, product):
        sleep(2)
        product_item_XPATH = configReader.readConfig("locators", "product_item_1_XPATH")+'"'+product+'"'+configReader.readConfig("locators", "product_item_2_XPATH")
        print(product_item_XPATH)
        # ScrollUtil.scrollToTextByAndroidUIAutomator(self.driver, product)
        self.click(product_item_XPATH)

    def addToCart(self):
        sleep(1)
        self.driver.implicitly_wait(10)
        self.click("add_to_cart_XPATH")

    def goToCart(self):
        sleep(5)
        self.driver.implicitly_wait(10)
        self.click("go_to_cart_XPATH")

    def placeOrder(self):
        sleep(2)
        self.driver.implicitly_wait(10)
        self.click("place_order_XPATH")

    def loginToApp(self, phone_number):
        sleep(1)
        self.driver.implicitly_wait(10)
        self.click("login_phone_id_XPATH")
        self.insertMobileNo()
        # self.type("login_phone_id_XPATH", phone_number)
        sleep(.5)
        self.click("continue_btn_XPATH")

    def continueOrder(self):
        sleep(1)
        self.click("continue_order_btn_XPATH")

    def enterCreditCardDetails(self, cc_no, cc_valid_year, cc_cvv):
        sleep(10)
        # ScrollUtil.scrollToTextByAndroidUIAutomator("Credit / Debit / ATM Card", self.driver)
        # ScrollUtil.scrollToText("com.flipkart.android:id/payments_root_view_id", "Credit / Debit / ATM Card", self.driver)
        ScrollUtil.swipeUp(1, self.driver)
        # ScrollUtil.swipeDown(1, self.driver)
        # ScrollUtil.scrollToInstance("android.view.View", self.driver)
        # self.click("cc_downArrow_XPATH")
        sleep(1)
        self.click("cc_no_XPATH")
        sleep(1)
        self.type("cc_no_XPATH", cc_no)
        sleep(1)
        self.click("cc_valid_year_XPATH")
        sleep(1)
        self.type("cc_valid_year_XPATH", cc_valid_year)
        sleep(1)
        self.click("cc_cvv_XPATH")
        sleep(1)
        self.type("cc_cvv_XPATH", cc_cvv)
        sleep(2)
        self.driver.hide_keyboard()
        # self.pressBack()
        sleep(5)
        self.click("pay_btn_XPATH")
        # self.pressEnter()
        sleep(5)
        # self.pressEnter()
        # self.click("pay_btn_XPATH")
        # sleep(5)

    def allowPermissions(self):
        # sleep(5)
        # self.click("allow_XPATH")
        # sleep(5)
        # self.click("permission_allow_XPATH")
        sleep(5)
        self.click("maybe_later_XPATH")
        sleep(40)
        # self.click("maybe_later_XPATH")
        print("Order Placed")
        log.logger.info("Order Placed")

    def orderPlaced(self):
        sleep(30)
        print("Order Placed")
        log.logger.info("Order Placed")

    def goToMessageApp(self, device):
        sleep(5)
        self.driver.implicitly_wait(30)
        if device == 'vivo':
            messageAppPackage = "com.android.mms"
        elif device == 'emulator':
            messageAppPackage = "com.google.android.apps.messaging"
        self.driver.activate_app(messageAppPackage)
        # self.switchActivity()
        self.driver.implicitly_wait(30)

    def terminateMessageApp(self, device):
        sleep(.5)
        if device == 'vivo':
            messageAppPackage = "com.android.mms"
        elif device == 'emulator':
            messageAppPackage = "com.google.android.apps.messaging"
        self.driver.terminate_app(messageAppPackage)
        sleep(.5)

    def backToFlipkartApp(self):
        sleep(.5)
        self.driver.implicitly_wait(30)
        self.driver.activate_app("com.flipkart.android")
        # self.switchActivity()
        self.driver.implicitly_wait(30)
        sleep(.5)

    def smsCount(self):
        sms = self.getElementCount("sms_conversation_name_XPATH")
        count = len(sms)
        print(count)
        log.logger.info("Total Element count " + str(count))
        for i in range(len(sms)):
            conversationName = self.getTextIndex("sms_conversation_name_XPATH", i)
            print(conversationName)
            if conversationName == 'arun jain':
                self.clickIndex("sms_conversation_name_XPATH", i)
                self.driver.implicitly_wait(30)
                text = self.getText("sms_text_XPATH")
                print(text)

                otp = re.findall(r'\b\d+\b', text)
                print(otp)

                self.pressBack()

    def otpRead(self, device):
        if device == 'vivo':
            self.driver.implicitly_wait(30)
            smsList = self.getElementCount("vivo_sms_list_XPATH")
            count = len(smsList)
            print(count)
            log.logger.info("Total Element count " + str(count))
            for i in range(len(smsList)):
                conversationName = self.getTextIndex("vivo_msg_sender_name_list_XPATH", i)
                print(conversationName)
                if 'VK-FLPKRT' in conversationName:
                    self.clickIndex("vivo_msg_sender_name_list_XPATH", i)
                    self.driver.implicitly_wait(30)
                    text = self.getText("vivo_last_msg_XPATH")
                    print(text)
                    otp = re.findall(r'\b\d+\b', text)
                    print("FLPKRT OTP is :: ", otp)
                    print(otp[0])
                    self.pressBack()
                    break
        elif device == 'emulator':
            self.driver.implicitly_wait(30)
            smsList = self.getElementCount("sms_list_XPATH")
            count = len(smsList)
            print(count)
            log.logger.info("Total Element count " + str(count))
            for i in range(len(smsList)):
                conversationName = self.getTextIndex("sms_conversation_name_XPATH", i)
                log.logger.info(conversationName)
                print(conversationName)
                if 'arun jain' in conversationName:
                    self.clickIndex("sms_conversation_name_XPATH", i)
                    self.driver.implicitly_wait(30)
                    text = self.getText("sms_text_XPATH")
                    log.logger.info(text)
                    otp = re.findall(r'\b\d+\b', text)
                    log.logger.info(otp)
                    print("FLPKRT OTP is :: ", otp)
                    log.logger.info("FLPKRT OTP is :: "+otp[0])
                    print(otp[0])
                    self.pressBack()
                    break

    def cancelOrder(self):
        sleep(2)
        # self.click("account_tab_XPATH")
        # sleep(.5)
        # self.click("orders_XPATH")
        # sleep(.5)
        self.click("cross_button_XPATH")
        sleep(.5)
        self.click("latest_oreder_item_XPATH")
        sleep(.5)
        self.click("edit_order_XPATH")
        sleep(.5)
        self.click("cancel_order_XPATH")
        sleep(.5)
        self.click("cancel_offer_order_XPATH")
        sleep(.5)
        self.click("my_reason_not_listed_XPATH")
        sleep(.5)
        self.type("comment_XPATH", "Not Like Product")
        sleep(.5)
        self.click("submit_request_XPATH")

    def getConfirmationOfCancellation(self):
        sleep(1)
        self.click("cross_button_XPATH")
        sleep(.5)
        text = self.getText("confirmation_XPATH")
        log.logger.info(text)

