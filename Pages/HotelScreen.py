import logging
import re
from time import sleep

from Pages.BasePage import BasePage

from Utilities.LogUtil import Logger
from Utilities.scroll_util import ScrollUtil

log = Logger(__name__, logging.INFO)


class HotelScreen(BasePage):

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

    def selectProduct(self):
        ScrollUtil.scrollToTextByAndroidUIAutomator("RPMSD Micro USB Cable 2 A 0.15 m 2 in 1 type c male and micro usb to USB Female otg cable", self.driver)
        # self.click("product_charger_XPATH")

    def addToCart(self):
        sleep(1)
        self.driver.implicitly_wait(10)
        self.click("add_to_cart_XPATH")

    def goToCart(self):
        sleep(2)
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
        sleep(5)
        # ScrollUtil.scrollToTextByAndroidUIAutomator("Credit / Debit / ATM Card", self.driver)
        # ScrollUtil.scrollToText("com.flipkart.android:id/payments_root_view_id", "Credit / Debit / ATM Card", self.driver)
        ScrollUtil.swipeUp(1, self.driver)
        # ScrollUtil.swipeDown(1, self.driver)
        # ScrollUtil.scrollToInstance("android.view.View", self.driver)
        self.click("cc_downArrow_XPATH")
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
        self.pressBack()
        sleep(5)
        # self.click("pay_btn_XPATH")
        self.pressEnter()
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

    def goToMessageApp(self):
        sleep(5)
        self.driver.implicitly_wait(30)
        vivoMessageAppPackage = "com.android.mms"
        emulatorMessageAppPackage = "com.google.android.apps.messaging"
        self.driver.activate_app(vivoMessageAppPackage)
        # self.switchActivity()
        self.driver.implicitly_wait(30)

    def terminateMessageApp(self):
        sleep(.5)
        vivoMessageAppPackage = "com.android.mms"
        emulatorMessageAppPackage = "com.google.android.apps.messaging"
        self.driver.terminate_app(vivoMessageAppPackage)
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

    def otpRead(self):
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
