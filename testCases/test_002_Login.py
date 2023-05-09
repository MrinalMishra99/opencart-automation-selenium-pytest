from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities import randomString
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class TestLogin():
    baseUrl = ReadConfig.get_application_url()
    logger = LogGen.loggen()

    user = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()

    def test_account_login(self, setUp):
        self.logger.info("**** test_002_Login started ****")
        self.driver = setUp
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.logger.info("**** Getting data from Home Page ****")
        self.home_page = HomePage(self.driver)
        self.home_page.clickAccountMyAccount()
        self.home_page.clickAccountLogin()
        self.logger.info("**** Getting data from Login Page ****")
        self.login_page = LoginPage(self.driver)
        self.login_page.setEmail(self.user)
        self.login_page.setPassWord(self.password)
        self.login_page.clickLogin()
        self.driver.close()
