import time

import pytest

from Pages.BasePage import BasePage
from Pages.HomeScreen import HomeScreen
from Pages.HotelScreen import HotelScreen
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider


class Test_SearchProduct(BaseTest):

    def test_searchProduct(self):
        # self.driver.implicitly_wait(30)
        home = HomeScreen(self.driver)
        # home.gotoSearchScreen().navigateToSearchScreen()
        home.gotoSearchScreen().searchForProduct("type c to micro usb connector")
        time.sleep(1)
        # home.gotoSearchScreen().closeNotificationPopup()
        # home.gotoSearchScreen().closeLocationPopup()
        home.gotoSearchScreen().selectProduct()
        home.gotoSearchScreen().addToCart()
        home.gotoSearchScreen().goToCart()
        home.gotoSearchScreen().placeOrder()

        # home.gotoSearchScreen().loginToApp("9754423998")
        home.gotoSearchScreen().goToMessageApp()
        home.gotoSearchScreen().otpRead()
        home.gotoSearchScreen().terminateMessageApp()
        home.gotoSearchScreen().backToFlipkartApp()
        home.gotoSearchScreen().continueOrder()
        # home.gotoSearchScreen().enterCreditCardDetails("4315813955699002", "02/30", "143")
        # home.gotoSearchScreen().allowPermissions()
