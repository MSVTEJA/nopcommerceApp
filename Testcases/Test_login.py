from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import pytest
from pageobjects.Loginpage import Login
from utilities.readproperities import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL=ReadConfig.getappURL()
    username=ReadConfig.getusername()
    password=ReadConfig.getpassword()

    logger=LogGen.loggen()  #calling the logger class


    @pytest.mark.regression
    def test_homepagetitle(self,setup):
        self.logger.info("*********Test_001_Login******")
        self.logger.info("******verifying homepage title*******")
        self.driver=setup
        self.driver.get(self.baseURL)
        actual_title=self.driver.title
        if actual_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*****Home page title is passed******")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homepagetitle.png")
            self.driver.close()
            assert False
            self.logger.info("*********Home page title is failed********")

    @pytest.mark.sanity
    @pytest.mark.reggression
    def test_login(self,setup):
        self.logger.info("****verifying login test*****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)         #creating object of Login class
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("****login test  is passed*****")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("*****login test is failed*****")
            assert False
