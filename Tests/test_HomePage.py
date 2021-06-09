from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_home(BaseTest):

    def test_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login_homepage(TestData.USER_NAME, TestData.PASSWORD)
        title = homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_home_page_header(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login_homepage(TestData.USER_NAME, TestData.PASSWORD)
        header = homePage.get_header_value()
        assert header == TestData.HOME_PAGE_HEADER

    def test_account_name(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login_homepage(TestData.USER_NAME, TestData.PASSWORD)
        account_name = homePage.get_account_name_value()
        assert account_name == TestData.ACCOUNT_NAME

    def test_settings_icon(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login_homepage(TestData.USER_NAME, TestData.PASSWORD)
        assert homePage.is_settings_icon_exist()
