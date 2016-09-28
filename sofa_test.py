

from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("http://root.test.customfurnish.com:8062/sofa")

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(5)
sofa_objects=driver.find_elements_by_class_name("sofa-grid-image")
print type(sofa_objects)

print "no of links are:",+len(sofa_objects)
for i in sofa_objects:
    print i.get_attribute("src")


k=7

while True:
    try:

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(5)
        sofa_objects = driver.find_elements_by_class_name("sofa-grid-image")
        size=len(sofa_objects)
        if sofa_objects[k].get_attribute("src")=='':
            print sofa_objects[k] + "Not Working!!!"
            continue

        else:
            sofa_objects[k].click()
            time.sleep(2)
            name_sofa=driver.find_element_by_xpath(".//*[@id='sofa_display_details']/div/div/div[1]/p").text
            print name_sofa
        text_path=driver.find_element_by_xpath(".//*[@id='sofa_display_details']/div/div/div[3]")
        text=text_path.text
        #print text
        text_len=len(text)
        print text_len

        if text_len>120:
            more_link=driver.find_element_by_xpath(".//*[@id='sofa_display_details']/div/div/div[3]/p/span[2]/a")
            if more_link.is_displayed():
                time.sleep(2)
                more_link.click()
                print "text length is",+text_len,"more----OK"
                time.sleep(4)

                more_link.click()
                time.sleep(3)

        if text_len<120:
            try:
                if driver.find_element_by_xpath(".//*[@id='sofa_display_details']/div/div/div[3]/p/span[2]/a").text=='more':
                    print "Not correct more is there "
            except Exception as e:
                print "text length is:",+text_len,"hence no more option"

        sofa_home = driver.find_element_by_xpath(".//*[@id='km-header']/div/nav/section/ul[1]/li[5]/a")
        sofa_home.click()
        time.sleep(2)

        k+=1
        #print "k val is :",+k
        #print "length is:",+size
        if k>size-1:
            break

    except Exception as e:
        print e