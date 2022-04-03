from selenium.webdriver.common.by import By

class SearchCustomer:
    txt_email_xpath="//input[@id='SearchEmail']"
    txt_fname_xpath="//input[@id='SearchFirstName']"
    txt_lname_xpath="//input[@id='SearchLastName']"
    btn_search_xpath=" //button[@id='search-customers']"
    table_xpath="//table[@id='customers-grid']"
    table_row_xpath="//table[@id='customers-grid']/tbody/tr"
    table_col_xpath="//table[@id='customers-grid']/tbody/tr/td"

    def __init__(self,driver):
        self.driver=driver

    def setemail(self,email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).clear()
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)

    def setfname(self,fname):
        self.driver.find_element(By.XPATH,self.txt_fname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_fname_xpath).send_keys(fname)

    def setlname(self,lname):
        self.driver.find_element(By.XPATH,self.txt_lname_xpath).clear()
        self.driver.find_element(By.XPATH,self.txt_lname_xpath ).send_keys(lname)
    def clicksearch(self):
        self.driver.find_element(By.XPATH,self.btn_search_xpath).click()
    def GetnoRow(self):
        return len(self.driver.find_elements(By.XPATH,self.table_row_xpath))
    def GetnoCol(self):
        return len(self.driver.find_elements(By.XPATH,self.table_col_xpath))
    def searchcustomerbyemail(self,email):
        flag=False
        for r in range(1,self.GetnoRow()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            emailid=self.driver.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid== email:
               flag=True
               break
            return flag

    def searchcustomerbyname(self,Name):
        flag = False
        for r in range(1, self.GetnoRow() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = self.driver.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
            return flag

