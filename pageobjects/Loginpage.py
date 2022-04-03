from selenium.webdriver.common.by import By
class Login:
    textbox_username_id="Email"
    textbox_password_id="Password"
    loginbutton_Xpath="//button[@class='button-1 login-button']"
    logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setusername(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.loginbutton_Xpath).click()

    def clicklogout(self):
        self.driver.find_element(By.LINK_TEXT,self.logout_linktext).click()





