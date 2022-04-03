import time
import pytest
from pageobjects.Loginpage import Login
from pageobjects.Addcustomerpage import AddCustomer
from pageobjects.searchCustomerpage import SearchCustomer
from utilities.readproperities import ReadConfig
from utilities.customLogger import LogGen
class Test_SearchCustomerByEmail_004:
    baseURL=ReadConfig.getappURL()
    username=ReadConfig.getusername()
    password=ReadConfig.getpassword()

    @pytest.mark.regression
    def test_searchcustomerbyemail(self,setup):
        print("************searchcustomerbyemail_004***********")
        self.driver=setup
        self.driver.get(self.baseURL)
            #login page
        self.lp=Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        print("**********loginsuccessful*********")

        #loging for customer section:
        self.addcustomer=AddCustomer(self.driver)
        self.addcustomer.ClickonCustomersMenu()
        self.addcustomer.ClickOnCustomersMenuItem()
        print("******searching customer by emailid********")
        searchcust=SearchCustomer(self.driver)
        searchcust.setemail("victoria_victoria@nopCommerce.com")
        searchcust.clicksearch()
        time.sleep(5)
        searchcust.searchcustomerbyemail("victoria_victoria@nopCommerce.com")
        status=searchcust.searchcustomerbyemail("victoria_victoria@nopCommerce.com")
        if status==True:
            print("******searchbyemailid is successful and test_004 fifnished************")

        self.driver.close()
