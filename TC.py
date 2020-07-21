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

#class TCALL():
#    def setUp():
#driver = webdriver.Chrome("/Users/scottmaretick/Desktop/chromedriver")
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
#TC1  ########################################LOG IN ##################################################
driver.get("https://portal-stg.celltrak.net/login")
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("caqa56")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("Dev1234@")
driver.find_element_by_id("submit").click()
driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot1.png');
#TC2 & TC3 ####################Check Schedules page showing the tab Admin > Schedules ####################
driver.find_element_by_css_selector("a.admin > span.icon").click()
#Name or ID = GABRIEL, G1319 (6044) - Patient
driver.get("https://portal-stg.celltrak.net/app/schedule")
driver.find_element_by_id("a6e600a5ea9ba02e0650bc6d7117f0d9").clear()
driver.find_element_by_id("a6e600a5ea9ba02e0650bc6d7117f0d9").send_keys("GABRIEL, G1319 (6044) - Patient")
driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot2.png');
#Schedule ID = SPV201611
driver.find_element_by_name("clientKey").clear()
driver.find_element_by_name("clientKey").send_keys("SPV201611")
driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot3.png');
#Date = 11/11/2016 - 11/13/2016
Select(driver.find_element_by_id("date_range_option")).select_by_visible_text("Specify...")
driver.find_element_by_css_selector("option[value=\"specify\"]").click()
driver.find_element_by_id("date_range_from").clear()
driver.find_element_by_id("date_range_from").send_keys("11/11/2016")
driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot4.png');
driver.find_element_by_id("date_range_to").clear()
driver.find_element_by_id("date_range_to").send_keys("11/13/2016")
time.sleep(5)
driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot5.png');
#HIT GO
time.sleep(5)
driver.find_element_by_xpath("//*[@id='filterApply']").click()
#############################################################################################
#Scroll to Location drop down
elementCT = driver.find_element_by_xpath(".//*[@id='recordFilter']/fieldset[6]/legend")
driver.execute_script("return arguments[0].scrollIntoView();", elementCT)
#DROP DOWN xpath=.//*[@id='ddcl-1']/span
driver.find_element_by_xpath(".//*[@id='ddcl-1']/span/span").click()  #OPENS LOCATION DROP DOWN
time.sleep(5)
#Location = CellTrak
driver.find_element_by_xpath("//*[@id='ddcl-1-ddw']/div/div[3]/label").click()  #SELECTS CellTrak
driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot4.png');
#Scroll to top of page (GO)
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(5)
#HIT GO
driver.find_element_by_xpath("//*[@id='filterApply']").click()
time.sleep(5)
#############################################################################################
#Scroll to Discipline drop down
elementDIS = driver.find_element_by_xpath(".//*[@id='recordFilter']/fieldset[7]/legend")
driver.execute_script("return arguments[0].scrollIntoView();", elementDIS)
#DROP DOWN xpath=.//*[@id='ddcl-1']/span
driver.find_element_by_xpath("//span[@id='ddcl-2']/span").click()  #OPENS DISCIPLINE DROP DOWN
#Discipline = HA
driver.find_element_by_xpath(".//*[@id='ddcl-2-ddw']/div/div[2]").click()
driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot5.png');
#Scroll to top of page (GO)
driver.execute_script("window.scrollTo(0, 0);")   #SCROLL TO TOP OF PAGE
time.sleep(5)
#HIT GO
driver.find_element_by_xpath("//*[@id='filterApply']").click()
time.sleep(5)
#############################################################################################
#Scroll to Program drop down
elementPRG= driver.find_element_by_xpath(".//*[@id='recordFilter']/fieldset[8]/legend")
driver.execute_script("return arguments[0].scrollIntoView();", elementPRG)
#DROP DOWN xpath=.//*[@id='ddcl-3']/span
driver.find_element_by_xpath(".//*[@id='ddcl-3']/span").click()
driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot6.png');
#Program = HA
driver.find_element_by_xpath(".//*[@id='ddcl-3-i2']").click()
#Scroll to top of page (GO)
driver.execute_script("window.scrollTo(0, 0);")   #SCROLL TO TOP OF PAGE
time.sleep(5)
driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot7.png');
#HIT GO
driver.find_element_by_xpath("//*[@id='filterApply']").click()
time.sleep(5)
#############################################################################################
driver.find_element_by_xpath(".//*[@id='schedule_recordset']/div[2]/div[1]/div[4]/a[2]").click() #OPENS DROPDOWN
driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot8.png');
#TC4 ######################### Record an activity for the schedule #############################
driver.find_element_by_xpath(".//*[@id='schedule_recordset']/div[2]/div[1]/div[4]/ul/li[1]/a/span").click() #SELECT AUDIT HISTORY
time.sleep(5)
driver.get("https://portal-stg.celltrak.net/app/schedule")
driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot9.png');
driver.find_element_by_xpath(".//*[@id='schedule_recordset']/div[2]/div[1]/div[4]/a[2]").click() #OPENS DROPDOWN (Patient ID:AALIYAH,A1693(7684))
time.sleep(5)
driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot10.png');
driver.find_element_by_xpath(".//*[@id='schedule_recordset']/div[2]/div[1]/div[4]/ul/li[2]/a/span").click() #OPENS & CLICKS "Record Activity"
time.sleep(5)
driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot11.png');
driver.find_element_by_xpath(".//*[@id='action_bar']/div/a[2]/span").click() #CLICKS NEXT ARROW
time.sleep(5)
driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot12.png');
driver.find_element_by_xpath(".//*[@id='action_bar']/div/a[2]/span").click() #CLICKS NEXT ARROW
time.sleep(25)
driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot13.png');
driver.find_element_by_xpath(".//*[@id='action_bar']/div/a[3]").click() #CLICK CANCEL
driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot14.png');
driver.find_element_by_xpath(".//*[@id='breadcrumbs']/ul/li[1]/a").click()  #GO TO ADMIN
driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot15.png');
driver.find_element_by_css_selector("li.schedule > a > div.icon").click()  # CLICK SCHEDULES
time.sleep(25)
driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot16.png');
###############################logout###################################
driver.get("https://portal-stg.celltrak.net/app/logout")
time.sleep(5)
#driver.find_element_by_xpath(".//*[@id='secondary_nav_my_account']/span").click()  #OPEN DROPDOWN
#driver.find_element_by_xpath(".//*[@id='secondary_nav_logout']").click()  #LOG OUT
driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot17.png');
driver.quit()
#############################################################################################
###driver.get(self.base_url + "/app/schedule")
#driver.find_element_by_id("date_range_to").click()  #OPEN TO DATE RANGE
#driver.find_element_by_xpath("(//a[contains(text(),'13')])[2]").click() #11/13/2016
#driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot10.png');
#driver.find_element_by_id("filterApply").click()
#driver.find_element_by_css_selector("a.view_logs > span").click()
#driver.find_element_by_xpath("(//a[contains(text(),'Cancel')])[8]").click()
#driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot10.png');
#driver.find_element_by_xpath("//div[@id='schedule_recordset']/div[2]/div[2]/div[4]/a[2]").click()
#driver.find_element_by_xpath("//div[@id='schedule_recordset']/div[2]/div[2]/div[4]/ul/li/a/span").click()
#driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot11.png');
#driver.find_element_by_xpath("(//a[contains(text(),'Cancel')])[8]").click()
#driver.find_element_by_css_selector("li.first > a").click()
#driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot12.png');
#driver.find_element_by_css_selector("#page_main > #activities_panel > ul > li.activity_closed > a > span").click()
#driver.find_element_by_link_text("Expand").click()
#driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot13.png');
#driver.find_element_by_link_text("Notes").click()
#driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot14.png');
#driver.find_element_by_xpath("(//a[contains(text(),'Close')])[3]").click()
#driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot15.png');
#driver.find_element_by_link_text("Expand").click()
#driver.find_element_by_css_selector("a[title=\"Download PDF\"] > span").click()
#driver.find_element_by_xpath("//div[@id='closed_activity_recordset']/div[2]/div[2]/div[4]/a[2]").click()
#driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot16.png');
#driver.find_element_by_xpath("//div[@id='closed_activity_recordset']/div[2]/div[2]/div[4]/ul/li[2]/a").click()
#driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot17.png');
#driver.find_element_by_xpath("//div[@id='closed_activity_recordset']/div[2]/div[2]/div[4]/a[2]").click()
#driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot18.png');
#driver.find_element_by_xpath("//div[@id='closed_activity_recordset']/div[2]/div[3]/div[4]/a[2]").click()
#driver.save_screenshot('//Users/scottmaretick/Desktop/SC_TC/ScreenShot19.png');
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#TC4 ######################### Record an activity for the schedule #############################
###Click on Record Activity

###Enter values In all the fields of pages displayed for recording Activity

###Save the Activity

#TC5 ############ Verify the status of the schedule once the recording is successful ##############
###On the schedule list page, verify that the status of the schedule is changed correctly





#TC6 ############################ Verify Schedule Details page ####################################
###Go to Admin > Schedules


###Enter ID of the Schedule in "Name or ID" edit box


###Click Go button


###Check the searched result


###Click on the magnifying glass icon on the searched Schedule


###Check the Schedule Details page showing tab Admin > Schedules > Schedule Details


###Verify the Patient Name, Patient ID, Schedule status, Schedule Time, Duration, Staff Name, Staff ID, Schedule





