
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest

driver=webdriver.Firefox()
driver.get("https://www.gmail.com/")
driver.maximize_window()
print(driver.title)
assert 'Gmail' in driver.title
user_name=driver.find_element_by_name('Email')
user_name.send_keys('srihari@kustommade.com')
driver.find_element_by_id('next').click()
passwd=driver.find_element_by_name('Passwd')
passwd.send_keys('Srihari@6278')
sign=driver.find_element_by_id('signIn')
sign.click()
#driver.implicitly_wait(20)

comp=driver.find_element_by_xpath(".//*[@id=':gi']/div/div")
comp.click()


driver.implicitly_wait(30)
mailid=driver.find_element_by_class_name("vO")
mailid.send_keys("sri.hari598@gmail.com")
subj=driver.find_element_by_class_name("aoT")
subj.send_keys("demo mail by srihari")

send=driver.find_element_by_xpath("//div[text()='Send']")
driver.implicitly_wait(10)
send.click()

try:
    WebDriverWait(driver,3).until(EC.alert_is_present(),'Time out waiting for PA creation')
    alert=driver.switch_to_alert()
    alert.accept()
except:
    print("no error")


driver.implicitly_wait(40)
nav=driver.find_element_by_xpath(".//*[@id='gb']/div[1]/div[1]/div[2]/div[4]/div[1]/a/span")
driver.implicitly_wait(40)
nav.click()

driver.implicitly_wait(20)
logout=driver.find_element_by_xpath(".//*[@id='gb_71']")

logout.click()


driver.implicitly_wait(20)




'''
class LoginTest(unittest.TestCase):
    def setUp(self):

        self.driver=webdriver.Firefox()
        self.driver.get("https://www.gmail.com/")


    def test_Login(self):
        driver = self.driver
        gmailUsername = 'srihari@kustommade.com'
        gmailPassword = 'Srihari@6278'
        emailFieldId="Email"
        passFieldId="passwd"
        loginButtonXpath="//input[@value='Sign in']"
        gmailLogoXpath="//a[contains(@href,'#inbox')]"


        emailFieldElement=WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(emailFieldId))
        passFieldElement=WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(passFieldId))
        loginButtonElement=WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_xpath(loginButtonXpath))

        emailFieldElement.clear()
        emailFieldElement.send_keys(gmailUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(gmailPassword)
        loginButtonElement.click()
        WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_xpath(gmailLogoXpath))

    def tearDown(self):
        self.driver.quit()
'''
