from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Firefox()
driver.get("http://www.customfurnish.com/chairs/?frameColor=natural_1_sheesham&fabric=fabric1")
time.sleep(3)


for i1 in range(1,24):#23
    frame_style=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[1]/div")
    frame_style.click()
    style=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]" % i1)
    #style.click()
    driver.execute_script("arguments[0].click();", style)
    style_name = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[1]/div/a[2]").text
    print "Frame Style:",style_name

    time.sleep(3)

    for i2 in range(1,4):#3
        material_tab = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[2]/div")
        material_tab.click()
        material=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]/img" % i2)
        material.click()
        material_name=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[2]/div/a[2]").text
        print "Material Name :", material_name
        time.sleep(2)

        for i3 in range(1,13):#12
            frame_color=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[3]/div")
            frame_color.click()
            color=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]/img" % i3)
            #color.click()
            driver.execute_script("arguments[0].click();", color)
            color_name=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[3]/div/a[2]").text
            print "color is:",color_name
            time.sleep(2)

            for i4 in range(1,59):#58
                fabric_tab=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[4]/div")
                fabric_tab.click()
                #driver.execute_script("window.scrollByLines(4)")
                #scroll=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul")

                #driver.execute_script("arguments[0].scrollIntoView(true);",list_field)
                #list_field = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul")
                fabric_item = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]/img" % i4)
                #list = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul")
                #driver.execute_script(list.location_once_scrolled_into_view)
                #driver.execute_script("return arguments[0].scrollIntoView();",fabric_item)
                #driver.execute_script("%s.scrollTo();" %list_field,fabric_item)
                driver.execute_script("arguments[0].click();",fabric_item)
                #driver.execute_script("fabric_item.location_once_scrolled_into_view")
                #actions=ActionChains(driver)
                #actions.move_to_element(fabric_item)
                #driver.execute_script("window.scrollTo(250,0);")
                fabric_name=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[4]/div/a[2]").text
                print "fabric is:",fabric_name
                #fabric_item.click()
                time.sleep(3)







