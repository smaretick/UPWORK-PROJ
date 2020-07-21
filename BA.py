# -*- coding: utf-8 -*-
#start BrowserStackLocal ./BrowserStackLocal MDKicy4nya2192zewKpz
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {'browser': 'firefox', 'FREELANCE': 'T1', 'browserstack.debug': 'true' }

browser = webdriver.Remote(
                          command_executor='http://scottmaretick2:MDKicy4nya2192zewKpz@hub.browserstack.com:80/wd/hub', #scottmaretick51
                          #command_executor='http://scottmaretick1:wWzHgVGrUqgDXdjZ5qKd@hub.browserstack.com:80/wd/hub', #Press Ganey
                          desired_capabilities=desired_cap)

#runs with either Firefox or Chrome
#browser = webdriver.Chrome("/Users/nickmaschinski/Desktop/chromedriver")  #V49.0.2623.112
#browser = webdriver.Firefox()  #V30.0
#browser.maximize_window()
browser.get("http://www.bloonaway.co.uk/")
#browser.find_element_by_xpath(".//*[@id='top']/body/div[3]/div/div[1]/div[1]/div/div[2]/a[2]/span").click() #BLOG
browser.get("http://www.bloonaway.co.uk/blog/")
browser.get("http://www.bloonaway.co.uk/prize-draw/")
browser.get("http://www.bloonaway.co.uk/shipping/")
browser.get("http://www.bloonaway.co.uk/privacy-policy/")
browser.get("http://www.bloonaway.co.uk/about-us/")
browser.get("http://www.bloonaway.co.uk/contacts/")
browser.get("http://www.bloonaway.co.uk/testimonials/")
browser.get("http://www.bloonaway.co.uk/guarantee/")
browser.get("http://www.bloonaway.co.uk/cashback/")
browser.quit()
