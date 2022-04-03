import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer:
#locators of webelements:
    link_customers_menu_xpath="//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]/p[1]"
    linkCustomer_menuitem_xpath="//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/p[1]"
    buttonAddNew_xpath="//a[@class='btn btn-primary']"
    textEmail_xpath="//input[@id='Email']"
    textPassword_xpath="//input[@id='Password']"
    txt_firstname_xpath=" //input[@id='FirstName']"
    txt_lastname_xpath="//input[@id='LastName']"
    rdMaleGender_xpath="//input[@id='Gender_Male']"
    rdFemaleGender_xpath="//input[@id='Gender_Female']"
    dateOfBith_xpath=" //input[@id='DateOfBirth']"
    txt_companyname_xpath="//input[@id='Company']"
    taxexemptCheckbox_xpath="//input[@id='IsTaxExempt']"
    txtAdmincontent_xpath="//textarea[@id='AdminComment']"
    drpManagervendor_xpath=" //select[@id='VendorId']"
    drpVendor1_visibletext="Vendor 1"
    txtCustomerRole_xpath="//ul[@id='SelectedCustomerRoleIds_taglist']"
    listitemGuest_xpath=" //li[contains(text(),'Guests')]"
    listitemVendors_xpath="//span[contains(text(),'Vendors')]"
    listitemRegister_xpath=" //span[contains(text(),'Registered')]"
    listitemAdministrators_xpath=" //span[contains(text(),'Administrators')]"
    NewsLetterYourstore_xpath="//option[contains(text(),'Your store name')]"
    btn_save_xpath="//body/div[3]/div[1]/form[1]/div[1]/div[1]/button[1]"

    def __init__(self,driver):
        self.driver=driver
    def ClickonCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.link_customers_menu_xpath).click()

    def ClickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH,self.linkCustomer_menuitem_xpath).click()

    def ClickOnAddnew(self):
        self.driver.find_element(By.XPATH,self.buttonAddNew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.textEmail_xpath).send_keys(email)
    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.textPassword_xpath).send_keys(password)
    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.txt_firstname_xpath).send_keys(fname)
    def setLastName(self,lname):
        self.driver.find_element(By.XPATH,self.txt_lastname_xpath).send_keys(lname)


    def setGender(self,gender):
        if gender=="Male":
            self.driver.find_element(By.XPATH,self.rdMaleGender_xpath).click()
        elif gender=="Female":
            self.driver.find_element(By.XPATH,self.rdFemaleGender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdMaleGender_xpath).click()

    def setDoB(self,dob):
        self.driver.find_element(By.XPATH,self.dateOfBith_xpath).send_keys(dob)

    def setCompanyName(self,cname):
        self.driver.find_element(By.XPATH,self.txt_companyname_xpath).send_keys(cname)

    def TaxexemptCheckbox(self):
        self.driver.find_element(By.XPATH,self.taxexemptCheckbox_xpath).click()

    def NewsLetter(self):
        self.driver.find_element(By.XPATH,self.NewsLetterYourstore_xpath).click()

    def CustomersRoles(self,role):
        self.driver.find_element(By.XPATH,self.txtCustomerRole_xpath).click()
        time.sleep(3)
        if role=="Registered":
            self.listitem=self.driver.find_element(By.XPATH,self.listitemRegister_xpath).click()
        elif role=="Vendors":
            self.listitem=self.driver.find_element(By.XPATH,self.listitemVendors_xpath).click()
        elif role=="Administrators":
            self.listitem=self.driver.find_element(By.XPATH,self.listitemAdministrators_xpath).click()
        elif role == "Guests":
            time.sleep(2)
            self.driver.find_element(By.XPATH,"//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.listitemGuest_xpath).click()
        elif role=="Registered":
            self.driver.find_element(By.XPATH,self.listitemRegister_xpath).click()
        elif role=="Vendors":
            self.listitem=self.driver.find_element(By.XPATH,self.listitemVendors_xpath).click()
        else:
            self.listitem=self.driver.find_element(By.XPATH, self.listitemGuest_xpath).click()
        time.sleep(2)
        #self.listitem.click()
        self.driver.execute_script("arguments[0].click();",self.listitem).click()

    def setManagerofvendor(self):
        drp=Select(self.driver.find_element(By.XPATH,self.drpManagervendor_xpath))
        drp.select_by_visible_text(self.drpVendor1_visibletext)

    def Admincontent(self,content):
        self.driver.find_element(By.XPATH,self.txtAdmincontent_xpath).send_keys(content)

    def ClickonSavebtn(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()