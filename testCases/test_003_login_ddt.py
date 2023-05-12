import time
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os


class Test_Login_DDT():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    path = os.path.abspath(os.curdir) + "\\testData\\Opencart_LoginData.xlsx"

    def test_login_ddt(self, setup):
        self.logger.info("**** Starting test_003_login_Datadriven *******")
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        lst_status = []

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)  # HomePage Page Object Class
        self.lp = LoginPage(self.driver)  # LoginPage Page Object Class
        self.ma = MyAccountPage(self.driver)  # MyAccount Page Object class

        for r in range(2, self.rows + 1):
            self.hp.clickAccountMyAccount()
            self.hp.clickAccountLogin()

            self.email = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setEmail(self.email)
            self.lp.setPassWord(self.password)
            self.lp.clickLogin()
            time.sleep(3)
            self.targetpage = self.lp.isMyAccountPageExists()

            if self.exp == 'Valid':
                if self.targetpage == True:
                    lst_status.append('Pass')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Fail')
            elif self.exp == 'Invalid':
                if self.targetpage == True:
                    lst_status.append('Fail')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Pass')
        self.driver.close()
        # final validation
        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("******* End of test_003_login_Datadriven **********")
