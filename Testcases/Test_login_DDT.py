import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import pytest
from pageobjects.Loginpage import Login
from utilities.readproperities import ReadConfig
from utilities.customLogger import LogGen
from utilities import xlutilities

class Test_002_DDT_Login:
    baseURL=ReadConfig.getappURL()
    path=".\\Testdata\\nop.xlsx"
    logger=LogGen.loggen()  #calling the logger class

    @pytest.mark.reggression
    def test_login_ddt(self,setup):
        self.logger.info("******TC002_DDt**************")
        self.logger.info("****verifying login test*****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)     #creating object of Login class
        self.rows= xlutilities.Getrowcount(self.path,'Sheet1')
        print("no of rows",self.rows)
        for r in range(2,self.rows+1):
            self.user=xlutilities.Readdata(self.path,'Sheet1',r,1)
            self.password=xlutilities.Readdata(self.path,'Sheet1',r,2)
            self.exp_result = xlutilities.Readdata(self.path,'Sheet1',r,3)

            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"
            list_status=[]

            if act_title==exp_title :
                if self.exp_result=='pass':
                    print("Test is passed")
                    self.lp.clicklogout()
                    list_status.append("pass")
                    self.logger.info("****login test  is passed*****")
                elif self.exp_result=="fail":
                    self.lp.clicklogout()
                    list_status.append("fail")
                    self.logger.info("*****login test is failed*****")
            elif act_title!=exp_title:
                if self.exp_result=="pass":
                    list_status.append("fail")
                elif self.exp_result=="fail":
                    list_status.append("pass")

        if "fail" not in list_status:
            print("DDT is passed")
            self.driver.close()
            assert True
        else:
            print("DDT is failed")
            self.driver.close()
            assert False