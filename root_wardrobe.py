from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Firefox()
driver.get("http://root.test.customfurnish.com/")
driver.maximize_window()


try:
    time.sleep(3)
    path=driver.find_element_by_xpath("//*[@id='SubscriptionModal']/a")
    path.click()

    '''
    email = driver.find_element_by_xpath("//*[@id='emailIdInModal']")
    email.send_keys('sri@gmail.com')
    btn=driver.find_element_by_xpath(".//*[@id='SubscriptionModal']/div/form/div[2]/div/a")
    btn.click()
    WebDriverWait(driver,4)
    alert=driver.switch_to_alert()
    alert.accept()
    WebDriverWait(driver,3)
    '''
except Exception as e:
    print 'exception found ',format(e)

print "--------------------wardrobe links----------------------------"
time.sleep(2)
ward1=driver.find_element_by_xpath(".//*[@id='km-header']/div/nav/section/ul[1]/li[2]/a")
url1=ward1.get_attribute('href')
ward1.click()
print url1+'  '+'--OK'
time.sleep(2)
home=driver.find_element_by_xpath("//*[@id='#body-wrapper']/div[2]/div/div[1]/a/img")
home.click()
time.sleep(2)
ward2=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[6]/div[3]/div[2]/ul/li[1]/a/img")
ward2.click()
url2=driver.current_url
if url1==url2:
    print url2+'  '+'--OK'
time.sleep(2)
home2=driver.find_element_by_xpath("//*[@id='#body-wrapper']/div[2]/div/div[1]/a/img")
home2.click()

ward3=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[6]/div[4]/div[5]/div/a/div")
ward3.click()
url3=driver.current_url
if url3=="http://root.test.customfurnish.com/wardrobe-designs/":
    print url3+'  '+'--OK'
home3=driver.find_element_by_xpath(".//*[@id='km-header']/div/nav/ul/li/a")
home3.click()


ward4=driver.find_element_by_xpath("//*[@id='body-wrapper']/div[6]/div[4]/div[5]/a/div")
ward4.click()
url4=driver.current_url
if url4==url3:
    print url4+'  '+'--OK'

home4=driver.find_element_by_xpath(".//*[@id='km-header']/div/nav/ul/li/a")
home4.click()

print "--------------------kitchen links---------------------------"
ktn1=driver.find_element_by_xpath(".//*[@id='km-header']/div/nav/section/ul[1]/li[3]/a")
ktn1.click()
kurl1=driver.current_url
print kurl1+'   '+'--OK'
khome1=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[2]/div/div[1]/a/img")
khome1.click()
ktn2=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[6]/div[3]/div[2]/ul/li[2]/a/img")
ktn2.click()
kurl2=driver.current_url
if kurl2=="http://root.test.customfurnish.com/kitchen-designer/step1/":
    print kurl2+'   '+'--OK'
time.sleep(3)
kclose_btn=driver.find_element_by_xpath("html/body/div[4]/a/span")
kclose_btn.click()
time.sleep(2)
khome2=driver.find_element_by_xpath("html/body/div[2]/div[2]/div/div[1]/a/img")
khome2.click()
ktn3=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[6]/div[4]/div[1]/a/div")
ktn3.click()
kurl3=driver.current_url
if kurl3=="http://root.test.customfurnish.com/kitchen/":
    print kurl3+'   '+'--OK'
khome3=driver.find_element_by_xpath(".//*[@id='km-header']/div/nav/ul/li/a")
khome3.click()
ktn4=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[6]/div[4]/div[1]/div/a[1]/div")
ktn4.click()
kurl4=driver.current_url
if kurl4==kurl3:
    print kurl4+'   '+'--OK'
driver.back()