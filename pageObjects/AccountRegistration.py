from selenium.webdriver.common.by import By


class AccountRegistration():
    txt_firstname_xpath = "//input[@name='firstname']"
    txt_lastname_xpath = "//input[@name='lastname']"
    txt_email_xpath = "//input[@name='email']"
    txt_password_xpath = '//*[@id="input-password"]'
    rad_subscribe_xpath = '//*[@id="input-newsletter-yes"]'
    chk_terms_xpath = '//*[@id="form-register"]/div/div/div/input'
    btn_register_xpath = '//*[@id="form-register"]/div/div/button'

    def __init__(self,driver):
        self.driver = driver


    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.txt_firstname_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH,self.txt_lastname_xpath).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)

    def setPassword(self,pwd):
        self.driver.find_element(By.XPATH,self.txt_password_xpath).send_keys(pwd)

    def setSubscription(self):
        self.driver.find_element(By.XPATH,self.rad_subscribe_xpath).click()

    def selectTerms(self):
        self.driver.find_element(By.XPATH,self.chk_terms_xpath).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH,self.btn_register_xpath).click()
