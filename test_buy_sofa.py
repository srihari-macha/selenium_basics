import unittest
from selenium import webdriver
import time
from proboscis import test

global window_before, window_after, total_price
class test_custom(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        driver=cls.driver
        driver.get("http://root.test.customfurnish.com/")
        print driver.title

    @test
    def test_1_home(self):
        driver=self.driver
        driver.maximize_window()
        time.sleep(10)
        close=driver.find_element_by_xpath(".//*[@id='SubscriptionModal']/a")
        close.click()
        time.sleep(5)
    @test
    def test_2_sofa(self):
        driver=self.driver
        sofa=driver.find_element_by_xpath(".//*[@id='km-header']/div/nav/section/ul[1]/li[5]/a")
        time.sleep(5)
        sofa.click()
        try:
            sofa_url=driver.current_url
            if sofa_url=="http://root.test.customfurnish.com/sofa":
                print "sofa page opened..."
        except:
            print "sofa page not opened..."
        time.sleep(2)
    @test
    def test_3_sofaimg(self):
        driver=self.driver
        time.sleep(4)
        sofa_img=driver.find_element_by_xpath(".//*[@id='variant-5785f0ae4b306433d77b986f']/div/div[1]/a/div[2]/section/img")
        sofa_img.click()
        time.sleep(6)
        order_set = driver.find_element_by_id("sofa-sets")
        order_set.click()
        time.sleep(3)
    @test
    def test_4_booknow(self):
        driver=self.driver
        book_button=driver.find_element_by_id("sofaBookNow")
        time.sleep(3)
        book_button.click()
        time.sleep(3)
    @test
    def test_5_pincode(self):
        driver=self.driver
        pincode=driver.find_element_by_name("pincode")
        pincode.send_keys("500046")
        time.sleep(3)
        check_button=driver.find_element_by_xpath(".//*[@id='sofaAvailabilityDropDown']/ul/input")
        check_button.click()
        time.sleep(6)
    @test
    def test_6_book(self):
        driver=self.driver
        book_now=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[2]/div[3]/div/div/div[2]/div[1]/a")
        driver.execute_script("window.scrollTo(0,400)")
        time.sleep(3)
        book_now.click()
        time.sleep(3)
    @test
    def test_7_login_link(self):
        driver=self.driver
        time.sleep(3)
        #global total_price
        #total_price=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[2]/div[3]/div/div/div[2]/ul[2]/li[2]").text
        #print "total price is:" +total_price
        global window_before
        window_before= driver.window_handles[0]
        print "window before is:" + window_before
        login_link=driver.find_element_by_xpath(".//*[@id='loginAtCheckOutModel']/div[4]/div[1]/div/ul[1]/li[2]/a")
        login_link.click()
        time.sleep(3)
        global total_price
        total_price = driver.find_element_by_xpath(
            ".//*[@id='body-wrapper']/div[5]/div[2]/div[3]/div/div/div[2]/ul[2]/li[2]").text
        print "total price is:" + total_price
        global window_after
        window_after=driver.window_handles[1]
        print "window after is :" +window_after
        driver.switch_to_window(window_after)
    @test
    def test_8_login(self):
        driver=self.driver
        time.sleep(5)
        username=driver.find_element_by_id("Email")
        username.send_keys("srihari@kustommade.com")
        btn=driver.find_element_by_id("next")
        btn.click()
        time.sleep(3)
        passwd=driver.find_element_by_id("Passwd")
        passwd.send_keys("Srihari@6278")
        sign_in=driver.find_element_by_id("signIn")
        sign_in.click()
        time.sleep(70)
    @test
    def test_9_details_payment(self):
        driver=self.driver


        driver.switch_to_window(window_before)
        try:
            time.sleep(2)
            okay_popup=driver.find_element_by_xpath(".//*[@id='cartModal']/div[2]/button")
            okay_popup.click()
            driver.execute_script("window.scrollTo(0,600)")
            time.sleep(6)
            global total_price
            total_price = driver.find_element_by_xpath(
                ".//*[@id='body-wrapper']/div[5]/div[2]/div[3]/div/div/div[2]/ul[2]/li[2]").text
            print "total_price is:" + total_price
            time.sleep(5)
            book_now=driver.find_element_by_xpath(".//*[@id='body-wrapper']/div[5]/div[2]/div[3]/div/div/div[2]/div[1]/a")
            time.sleep(3)
            book_now.click()
            time.sleep(3)

        except:
            print "in except in test case-9"

        pay_price=driver.find_element_by_xpath(".//*[@id='crat-summary-details']/tbody/tr[7]/td[2]").text
        print "pay_price is: " +pay_price

        try:
            if total_price==pay_price:
                print "prices are same...."
            else:
                print "prices are not same"
                return
        except:
            pass
        pay_button=driver.find_element_by_id("saveDetails")
        pay_button.click()
        time.sleep(3)
        pay=driver.find_element_by_id("ebsPay")
        pay.click()
        time.sleep(8)


        '''
        driver.switch_to_window(window_before)
        check_address=driver.find_element_by_id("new-addr-label")
        check_address.click()
        time.sleep(5)
        name=driver.find_element_by_id("shippingName")
        name.send_keys("abc")
        phone=driver.find_element_by_id("shippingPhone")
        phone.send_keys("9440123456")
        address=driver.find_element_by_id("shippingAddressLines")
        address.send_keys("Hyderabad")
        pincode=driver.find_element_by_id("shippingPincode")
        pincode.send_keys("500046")
        city=driver.find_element_by_id("shippingCity")
        city.send_keys("Hyderabad")
        driver.find_element_by_xpath("//select[@name='state']/option[text()='Telangana']").click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(400,30)")
        pay_now=driver.find_element_by_id("saveDetails")
        time.sleep(3)
        pay_now.click()
        time.sleep(3)
        pay = driver.find_element_by_id("ebsPay")
        pay.click()
        time.sleep(8)
        '''

    @test
    def test_9_payment(self):
        driver=self.driver
        name_card=driver.find_element_by_id("frm_name_on_card")
        name_card.send_keys("customfurnish")
        card_num1=driver.find_element_by_name("number_1")
        card_num1.send_keys("4111")
        card_num2 = driver.find_element_by_name("number_2")
        card_num2.send_keys("1111")
        card_num3 = driver.find_element_by_name("number_3")
        card_num3.send_keys("1111")
        card_num4 = driver.find_element_by_name("number_4")
        card_num4.send_keys("1111")
        time.sleep(3)
        driver.find_element_by_xpath("//select[@name='exp_month']/option[text()='07 (Jul)']").click()
        driver.find_element_by_xpath("//select[@name='exp_year']/option[text()='2017']").click()
        cvv_num=driver.find_element_by_id("frm_cvv")
        cvv_num.send_keys("123")
        time.sleep(3)
        pay_btn=driver.find_element_by_id("submitted")
        #pay_btn.click()
        time.sleep(8)







    '''
    def test_order_set(self):
        time.sleep(3)
        driver=self.driver
        order_set=driver.find_element_by_id("sofa-sets")
        order_set.click()
    '''

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__=='__main__':
    unittest.main()