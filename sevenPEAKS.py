# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import unittest, time, re

#driver = webdriver.Chrome("/Users/scottmaretick/Desktop/chromedriver")
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
#########################################LOG IN ##################################################
driver.get("https://sevenpeaks.aluvii.com/guest/")
driver.find_element_by_id("txtUsername").send_keys("scottmaretick51@gmail.com")
#.//*[@id='txtUsername']
driver.find_element_by_id("txtPassword").send_keys("Sm110751!")
#.//*[@id='txtPassword']
time.sleep(10);
driver.find_element_by_id("btnSubmit").click()
#.//*[@id='btnSubmit']
#CHECK OUT YOUR PASSES
#
driver.find_element_by_xpath(".//*[@id='dashboard-quick-links']/div[1]/a").click()
driver.find_element_by_xpath(".//*[@id='membership-passes']/form/div[2]/div/span").click()
#POP UP COMES UP
window1 = driver.window_handles[0]
print window1
driver.switch_to.window(window1)
#Now you are in the popup window, perform necessary actions here
driver.quit()
