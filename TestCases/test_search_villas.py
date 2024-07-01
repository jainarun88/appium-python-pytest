import pytest

from Pages.HomeScreen import HomeScreen
from Pages.HotelScreen import HotelScreen
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
from Utilities.scroll_util import ScrollUtil


class Test_SearchVilla(BaseTest):

    # @pytest.mark.parametrize("city,hotel", dataProvider.get_data("VillaTest"))
    def test_searchVilla(self):
        home = HomeScreen(self.driver)
        home.gotoSearchScreen().navigateToSearchScreen()
        # home.gotoVillas().searchVilla(city)
        # ScrollUtil.scrollToTextByAndroidUIAutomator(hotel, self.driver)