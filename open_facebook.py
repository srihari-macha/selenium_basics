from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get('https://www.facebook.com')
driver.maximize_window()
print(driver.title)
assert 'Facebook' in driver.title
username=driver.find_element_by_xpath("//input[@id='email']")
username.send_keys('sri.hari6278@hotmail.com')
#username.clear()
username=driver.find_element_by_xpath("//input[@id='pass']")
username.send_keys('machasrihari')
#username.clear()
#driver.find_element_by_id('email').send_keys('sri.hari6278@hotmail.com')
#driver.find_element_by_id('pass').send_keys('srihari')
login=driver.find_element_by_xpath(".//*[@id='u_0_l']")

login.click()
#driver.find_element_by_id('loginbutton').click()

navi=driver.find_element_by_xpath(".//*[@id='pageLoginAnchor']")

#navi=driver.find_element_by_id('userNavigationLabel')
navi.click()
driver.implicitly_wait(40)
logout=driver.find_element_by_xpath(".//*[@id='BLUE_BAR_ID_DO_NOT_USE']/div/div/div[1]/div/div/ul/li[12]/a/span/span")
#logout=driver.find_element_by_xpath(".//*[@id='BLUE_BAR_ID_DO_NOT_USE']/div/div/div[1]/div/div/ul/li[12]/a/span/span").navi.click()

logout.click()
driver.implicitly_wait(40)

#logout=driver.find_element_by_tag_name('Log Out')
#logout.click()

