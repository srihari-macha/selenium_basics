from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://root.test.customfurnish.com/")
wardrobe=driver.find_element_by_xpath(".//*[@id='km-header']/div/nav/section/ul[1]/li[2]/a")
url1=wardrobe.get_attribute('href')
wardrobe.click()
if url1 == 'http://root.test.customfurnish.com/wall-profile/wardrobe-type':
    print url1+'   '+'--'+'OK'
else:
    print url1 + '   ' + '--' + 'NO'

wrdrobe_dim=driver.find_element_by_xpath(".//*[@id='#body-wrapper']/div[7]/div[3]/div[2]/div/a")
url2=wrdrobe_dim.get_attribute('href')
wrdrobe_dim.click()
if url2=='http://root.test.customfurnish.com/wall-profile/dimensions':
    print url2 + '   ' + '--' + 'OK'
else:
    print url2 + '   ' + '--' + 'NO'

wrdrobe_sub_dim=driver.find_element_by_xpath(".//*[@id='submitWallDimension']")
wrdrobe_sub_dim.click()
url3= driver.current_url
if 'http://root.test.customfurnish.com/wall-profile/layout?design' in url3:
    print url3 + '   ' + '--' + 'OK'
else:
    print url3 + '   ' + '--' + 'NO'

wrdrobe_design=driver.find_element_by_xpath(".//*[@id='wallLayoutSubmit']")
wrdrobe_design.click()
url4=driver.current_url
if url3==url4:
    print url4 + '   ' + '--' + 'OK'
else:
    print url4 + '   ' + '--' + 'NO'

wrdrobe_door=driver.find_element_by_xpath(".//*[@id='#body-wrapper']/div[7]/div[2]/div[3]/div[2]/div[1]/div[1]/a")
wrdrobe_door.click()
url5=driver.current_url
if 'http://root.test.customfurnish.com/wall-profile/layout-with-designs?design' in url5:
    print url5 + '   ' + '--' + 'OK'
else:
    print url5 + '   ' + '--' + 'NO'

wrdrobe_interior=driver.find_element_by_xpath(".//*[@id='wallInternalDesignMode']")
wrdrobe_interior.click()
buy_btn=driver.find_element_by_xpath(".//*[@id='buyNow']")
buy_btn.click()
url6=driver.current_url
if 'http://root.test.customfurnish.com/wall-profile/hardware?design' in url6:
    print url6 + '   ' + '--' + 'OK'
else:
    print url6 + '   ' + '--' + 'NO'

