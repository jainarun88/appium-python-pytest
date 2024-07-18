from Pages.BasePage import BasePage
from Pages.ProductScreen import ProductScreen


class HomeScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def gotoSearchScreen(self):
        return ProductScreen(self.driver)


