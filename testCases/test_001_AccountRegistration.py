import time

from pageObjects.AccountRegistration import AccountRegistration
from pageObjects.HomePage import HomePage
from utilities import randomString
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class TestAccountRegistrationPage:
    basUrl = ReadConfig.get_application_url()
    logger = LogGen.loggen()

    def test_account_reg(self, setUp):
        self.logger.info("**** test_001_AccountRegistration started ****")
        self.driver = setUp
        self.driver.get(self.basUrl)
        self.logger.info("**** launching application ****")
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickAccountMyAccount()
        self.hp.clickAccountRegister()

        self.logger.info("*** Here we are filling up the registration form ***")
        self.rp = AccountRegistration(self.driver)
        self.rp.setFirstName("mr")
        self.rp.setLastName("Mishra")
        self.email = randomString.random_string_generator() + '@gmail.com'
        self.rp.setEmail(self.email)
        self.rp.setPassword("password")
        time.sleep(8)
        self.rp.setSubscription()
        self.rp.selectTerms()
        self.rp.clickContinue()
        self.driver.close()
