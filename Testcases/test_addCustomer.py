import string
from selenium.webdriver.common.by import By
import pytest
import time
import random
from pageobjects.Addcustomerpage import AddCustomer
from pageobjects.Loginpage import Login
from utilities.readproperities import ReadConfig
class Test_TC003_Addcustomer:
    baseURL=ReadConfig.getappURL()
    Username=ReadConfig.getusername()
    Password=ReadConfig.getpassword()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addcustomer(self,setup):
        #using setup fixture
        print("**********Test_TC003_Addcustomer************")
        self.driver=setup
        self.driver.get(self.baseURL)

        #logging the page
        self.lp=Login(self.driver)     #loginpage object creation
        self.lp.setusername(self.Username)
        self.lp.setpassword(self.Password)
        self.lp.clicklogin()
        print("*********login successful********")

        #adding new customer test
        self.addcust=AddCustomer(self.driver) #creating object for add customer
        self.addcust.ClickonCustomersMenu()
        self.addcust.ClickOnCustomersMenuItem()

        self.addcust.ClickOnAddnew()

        print("********providing newcustomer info**********")
        self.email=random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test003")
        self.addcust.setFirstName("vishnu")
        self.addcust.setLastName("teja")
        self.addcust.setGender("Male")
        self.addcust.setDoB("03/13/1960")
        self.addcust.setCompanyName("tcs")
        self.addcust.TaxexemptCheckbox()
        #self.addcust.CustomersRoles("Vendors")
        self.addcust.setManagerofvendor()
        self.addcust.Admincontent("first test")
        time.sleep(2)
        self.addcust.ClickonSavebtn()

        print("*******saving customer info********")
        print("******add customer validation*******")

        self.infom = self.driver.find_element(By.TAG_NAME("body")).text
        print(self.infom)

        if "The new customer has been added successfully" in (self.infom):
            assert True
            print("test is passed")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"testcustomer_scr.png")
            assert False
            print("unsuccessful test")

        self.driver.close()
        print("*******ending addcust testing TC003*******************")

def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return "".join(random.choice(chars)for x in range(size))
