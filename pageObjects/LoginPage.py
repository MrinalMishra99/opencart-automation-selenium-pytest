from selenium.webdriver.common.by import By


class LoginPage():
    txt_email_xpath = '//*[@id="input-email"]'
    txt_pass_xpath = '//*[@id="input-password"]'
    btn_login_xpath = '//*[@id="form-login"]/button'

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, mail):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(mail)

    def setPassWord(self,pwd):
        self.driver.find_element(By.XPATH,self.txt_pass_xpath).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()