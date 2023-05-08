from selenium.webdriver.common.by import By


class HomePage():
    # Locators
    lnk_myacount_linktext = 'My Account'
    lnk_register_linktext = 'Register'
    lnk_login_linktext = 'Login'

    # Constructors
    def __init__(self, driver):
        self.driver = driver

    # Actions
    def clickAccountMyAccount(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_myacount_linktext).click()

    def clickAccountRegister(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_register_linktext).click()

    def clickAccountLogin(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_login_linktext).click()
