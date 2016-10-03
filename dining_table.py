from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("http://www.customfurnish.com/tables/?legColor=natural_1_sheesham&topColor=natural_1_sheesham")
time.sleep(3)


for i1 in range(1,4): #3
    shape_tab = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[1]/div")
    shape_tab.click()

    shape_type=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]/img" % i1)
    shape_type.click()
    time.sleep(2)
    shape_text=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[1]/div/a[2]").text
    print "shape is:",shape_text
    #list_size=driver.find_elements_by_css_selector("more-designs-image ")
    size_tab=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[2]/div")
    size_tab.click()
    time.sleep(2)
    size_text=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[2]/div/a[2]").text
    print "size is:", size_text
    list_size=driver.find_elements_by_class_name("more-designs-image")
    size=len(list_size)
    #print type(list_size)
    #print size

    for i2 in range(1,size+1):
        size_tab=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[2]/div")
        size_tab.click()
        size_type=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]/img" % i2)
        driver.execute_script("arguments[0].click();",size_type)
        time.sleep(2)
        try:
            if i1==1:
                #print "leg design disabled!!!"
                pedestal_tab=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[4]/div")
                pedestal_tab.click()
                pedestal_items_size=driver.find_elements_by_class_name("more-designs-image")
                pedestal_size=len(pedestal_items_size)

                for i4 in range(1,pedestal_size+1):
                    pedestal_tab = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[4]/div")
                    pedestal_tab.click()
                    pedestal_item=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]/img" % i4)
                    pedestal_item.click()
                    pedestal_text=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[4]/div/a[2]").text
                    print "Pedestal Design: ",pedestal_text
                    time.sleep(2)

                    top_material_tab = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div")
                    top_material_tab.click()
                    top_material_size = driver.find_elements_by_class_name("more-designs-image")
                    top_size = len(top_material_size)

                    for i5 in range(1, top_size + 1):
                        top_material_tab = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div")
                        top_material_tab.click()
                        top_item = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]/img" % i5)
                        top_item.click()
                        top_material_text=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div/a[2]").text
                        print "Material is:", top_material_text
                        time.sleep(2)

                        top_color_tab=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div")
                        top_color_tab.click()
                        top_color_size=driver.find_elements_by_class_name("more-designs-image")
                        color_size=len(top_color_size)

                        for i6 in range(1,color_size+1):
                            top_color_tab = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div")
                            top_color_tab.click()
                            color_item=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]/img" % i6)
                            driver.execute_script("arguments[0].click();", color_item)
                            color_text=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div/a[2]").text
                            print "Top color is :",color_text
                            time.sleep(2)

                            leg_material_tab=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div")
                            leg_material_tab.click()
                            leg_material_size=driver.find_elements_by_class_name("more-designs-image")
                            material_size=len(leg_material_size)

                            for i7 in range(1,material_size+1):
                                leg_material_tab = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div")
                                leg_material_tab.click()
                                material_item=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]/img" % i7)
                                material_item.click()
                                leg_text=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div/a[2]").text
                                print "Leg Material is:",leg_text
                                time.sleep(2)

                                leg_color_tab=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div")
                                leg_color_tab.click()
                                leg_color_size=driver.find_elements_by_class_name("more-designs-image")
                                new_color_size=len(leg_color_size)

                                for i8 in range(1, new_color_size+1):
                                    leg_color_tab = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div")
                                    leg_color_tab.click()
                                    leg_color_item=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]/img" % i8)
                                    driver.execute_script("arguments[0].click();",leg_color_item)
                                    time.sleep(2)
                                    leg_color_text=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div/a[2]").text
                                    print "Leg color is",leg_color_text




            if i1==2:
                print "i1 val is:", i1

                #print "pedestal design disabled!!!"
                leg_tab=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[3]/div")
                leg_tab.click()
                leg_items_size=driver.find_elements_by_class_name("more-designs-image")
                leg_size=len(leg_items_size)

                for i3 in range(1,leg_size+1):
                    leg_tab = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[3]/div")
                    leg_tab.click()
                    leg_item=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]/img" % i3)
                    driver.execute_script("arguments[0].click();",leg_item)
                    time.sleep(2)

                    top_material_tab = driver.find_element_by_xpath(
                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div")
                    top_material_tab.click()
                    top_material_size = driver.find_elements_by_class_name("more-designs-image")
                    top_size = len(top_material_size)

                    for i5 in range(1, top_size + 1):
                        top_material_tab = driver.find_element_by_xpath(
                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div")
                        top_material_tab.click()
                        top_item = driver.find_element_by_xpath(
                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]/img" % i5)
                        top_item.click()
                        top_material_text = driver.find_element_by_xpath(
                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div/a[2]").text
                        print "Material is:", top_material_text
                        time.sleep(2)

                        top_color_tab = driver.find_element_by_xpath(
                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div")
                        top_color_tab.click()
                        top_color_size = driver.find_elements_by_class_name("more-designs-image")
                        color_size = len(top_color_size)

                        for i6 in range(1, color_size + 1):
                            top_color_tab = driver.find_element_by_xpath(
                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div")
                            top_color_tab.click()
                            color_item = driver.find_element_by_xpath(
                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]/img" % i6)
                            driver.execute_script("arguments[0].click();", color_item)
                            color_text = driver.find_element_by_xpath(
                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div/a[2]").text
                            print "Top color is :", color_text
                            time.sleep(2)

                            leg_material_tab = driver.find_element_by_xpath(
                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div")
                            leg_material_tab.click()
                            leg_material_size = driver.find_elements_by_class_name("more-designs-image")
                            material_size = len(leg_material_size)

                            for i7 in range(1, material_size + 1):
                                leg_material_tab = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div")
                                leg_material_tab.click()
                                material_item = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]/img" % i7)
                                material_item.click()
                                leg_text = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div/a[2]").text
                                print "Leg Material is:", leg_text
                                time.sleep(2)

                                leg_color_tab = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div")
                                leg_color_tab.click()
                                leg_color_size = driver.find_elements_by_class_name("more-designs-image")
                                new_color_size = len(leg_color_size)

                                for i8 in range(1, new_color_size + 1):
                                    leg_color_tab = driver.find_element_by_xpath(
                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div")
                                    leg_color_tab.click()
                                    leg_color_item = driver.find_element_by_xpath(
                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]/img" % i8)
                                    driver.execute_script("arguments[0].click();", leg_color_item)
                                    time.sleep(2)
                                    leg_color_text = driver.find_element_by_xpath(
                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div/a[2]").text
                                    print "Leg color is", leg_color_text


            if i1==3:

                leg_tab = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[3]/div")
                leg_tab.click()
                leg_items_size = driver.find_elements_by_class_name("more-designs-image")
                leg_size = len(leg_items_size)

                for i3 in range(1, leg_size + 1):
                    leg_tab = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[3]/div")
                    leg_tab.click()
                    leg_item = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]/img" % i3)
                    driver.execute_script("arguments[0].click();", leg_item)
                    time.sleep(2)

                    top_material_tab = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div")
                    top_material_tab.click()
                    top_material_size = driver.find_elements_by_class_name("more-designs-image")
                    top_size = len(top_material_size)

                    pedestal_tab = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[4]/div")
                    pedestal_tab.click()
                    pedestal_items_size = driver.find_elements_by_class_name("more-designs-image")
                    pedestal_size = len(pedestal_items_size)

                    for i4 in range(1, pedestal_size + 1):
                        pedestal_tab = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[4]/div")
                        pedestal_tab.click()
                        pedestal_item = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]/img" % i4)
                        pedestal_item.click()
                        pedestal_text = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[4]/div/a[2]").text
                        print "Pedestal Design: ", pedestal_text
                        time.sleep(2)

                        top_material_tab = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div")
                        top_material_tab.click()
                        top_material_size = driver.find_elements_by_class_name("more-designs-image")
                        top_size = len(top_material_size)

                        for i5 in range(1, top_size + 1):
                            top_material_tab = driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div")
                            top_material_tab.click()
                            top_item = driver.find_element_by_xpath(
                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]/img" % i5)
                            top_item.click()
                            top_material_text = driver.find_element_by_xpath(
                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[5]/div/a[2]").text
                            print "Material is:", top_material_text
                            time.sleep(2)

                            top_color_tab = driver.find_element_by_xpath(
                                ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div")
                            top_color_tab.click()
                            top_color_size = driver.find_elements_by_class_name("more-designs-image")
                            color_size = len(top_color_size)

                            for i6 in range(1, color_size + 1):
                                top_color_tab = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div")
                                top_color_tab.click()
                                color_item = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]/img" % i6)
                                driver.execute_script("arguments[0].click();", color_item)
                                color_text = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[6]/div/a[2]").text
                                print "Top color is :", color_text
                                time.sleep(2)

                                leg_material_tab = driver.find_element_by_xpath(
                                    ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div")
                                leg_material_tab.click()
                                leg_material_size = driver.find_elements_by_class_name("more-designs-image")
                                material_size = len(leg_material_size)

                                for i7 in range(1, material_size + 1):
                                    leg_material_tab = driver.find_element_by_xpath(
                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div")
                                    leg_material_tab.click()
                                    material_item = driver.find_element_by_xpath(
                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]/img" % i7)
                                    material_item.click()
                                    leg_text = driver.find_element_by_xpath(
                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[7]/div/a[2]").text
                                    print "Leg Material is:", leg_text
                                    time.sleep(2)

                                    leg_color_tab = driver.find_element_by_xpath(
                                        ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div")
                                    leg_color_tab.click()
                                    leg_color_size = driver.find_elements_by_class_name("more-designs-image")
                                    new_color_size = len(leg_color_size)

                                    for i8 in range(1, new_color_size + 1):
                                        leg_color_tab = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div")
                                        leg_color_tab.click()
                                        leg_color_item = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[1]/cf-options/ul/li[%d]/img" % i8)
                                        driver.execute_script("arguments[0].click();", leg_color_item)
                                        time.sleep(2)
                                        leg_color_text = driver.find_element_by_xpath(
                                            ".//*[@id='body-wrapper']/div[5]/div[1]/div/div[2]/cf-toolbar/div/div[8]/div/a[2]").text
                                        print "Leg color is", leg_color_text


        except Exception as e:
            print e










