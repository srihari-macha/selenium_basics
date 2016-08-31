from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import linkGrabber
import httplib
import urllib


driver=webdriver.Firefox()
driver.get("http://root.test.customfurnish.com/")
#driver.maximize_window()
list_tags=driver.find_elements_by_tag_name("a")
print 'total links are :',len(list_tags)

links=driver.find_elements_by_tag_name("a")
passed=0
failed=0
for i in links:
    url=i.get_attribute('href')
    #print url
    try:
        val=urllib.urlopen(url).getcode()
        if val==200:
            print url+'   '+'-'+'OK'
            passed+=1

        else:
            print url+'   '+'-'+'NO'
            failed+=1



    except(Exception ):
        pass

print 'Total links working:',+passed
print 'Total links not working:',+failed






