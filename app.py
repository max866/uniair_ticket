# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://www.uniair.com.tw/rwd/B2C/booking/ubk_search.aspx")
        driver.find_element_by_id("ddl_DEP").click()
        Select(driver.find_element_by_id("ddl_DEP")).select_by_visible_text(u"台中(RMQ)")
        driver.find_element_by_xpath("//option[@value='RMQ']").click()
        driver.find_element_by_id("ddl_ARR").click()
        Select(driver.find_element_by_id("ddl_ARR")).select_by_visible_text(u"南竿(LZN)")
        driver.find_element_by_xpath("(//option[@value='LZN'])[2]").click()
        
        driver.find_element_by_id("CPH_Body_div_TripDate").click()
        driveer.find_element_by_css_selector('.-input.-datepicker.active').click()
        

        driver.find_element_by_id("CPH_Body_tb_TripDate").click()
        driver.find_element_by_id("CPH_Body_hi_TRIP_DATE").click()
        Select(driver.find_element_by_name("CPH_Body_hi_TRIP_DATE")).select_by_visible_text(u"2020/08/09")
        
        driver.find_element_by_id("CPH_Body_tb_PaxNum").click()
        driver.find_element_by_xpath("//div[@id='CPH_Body_div_PaxNum']/div/div/div/div[2]/div/div[3]/button").click()
        driver.find_element_by_xpath("//div[@id='CPH_Body_div_PaxNum']/div/div/div/div[2]/div/div[3]/button").click()
        driver.find_element_by_xpath("//div[@id='CPH_Body_div_PaxNum']/div/div/div/div[2]/div/div[3]/button").click()
        driver.find_element_by_xpath("//div[@id='CPH_Body_div_PaxNum']/div/button").click()
        

        # driver.find_element_by_id("CPH_Body_txt_CaptchaCode").click()
        # driver.find_element_by_id("CPH_Body_txt_CaptchaCode").clear()
        # driver.find_element_by_id("CPH_Body_txt_CaptchaCode").send_keys("345056")
        # driver.find_element_by_id("CPH_Body_btn_SelectFlight").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
