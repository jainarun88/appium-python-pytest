import time

import pytest

from Pages.BasePage import BasePage
from Pages.HomeScreen import HomeScreen
from Pages.ProductScreen import ProductScreen
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
from Utilities.ExcelReader import getCellData


class Test_SearchProduct(BaseTest):

    def test_searchProduct(self):
       
        path = "excel//testdata.xlsx"
        sheetProductSearch = "ProductSearch"
        sheetCardDetails = "CardDetails"

        productName = getCellData(path,sheetProductSearch,2,1)
        print(productName)
        creditCardNumber = getCellData(path,sheetCardDetails,2,2)
        creditCardExpiry = getCellData(path,sheetCardDetails,2,3)
        creditCardCVV = getCellData(path,sheetCardDetails,2,4)
        print(creditCardNumber)
        print(creditCardExpiry)
        print(creditCardCVV)

        # self.driver.implicitly_wait(30)
        home = HomeScreen(self.driver)
        # home.gotoSearchScreen().navigateToSearchScreen()
        home.gotoSearchScreen().searchForProduct(productName)
        time.sleep(1)
        # home.gotoSearchScreen().closeNotificationPopup()
        # home.gotoSearchScreen().closeLocationPopup()
        home.gotoSearchScreen().selectProduct(productName)
        home.gotoSearchScreen().addToCart()
        home.gotoSearchScreen().goToCart()
        home.gotoSearchScreen().placeOrder()

        # home.gotoSearchScreen().loginToApp("9754423998")
        home.gotoSearchScreen().continueOrder()
        home.gotoSearchScreen().enterCreditCardDetails(creditCardNumber, creditCardExpiry, creditCardCVV)
        home.gotoSearchScreen().allowPermissions()
        home.gotoSearchScreen().goToMessageApp('emulator')
        otp = home.gotoSearchScreen().otpRead('emulator')
        # home.gotoSearchScreen().terminateMessageApp('emulator')
        home.gotoSearchScreen().backToFlipkartApp()
        home.gotoSearchScreen().enterOTP(otp)
        home.gotoSearchScreen().orderPlaced()
        home.gotoSearchScreen().cancelOrder()
        home.gotoSearchScreen().getConfirmationOfCancellation()
