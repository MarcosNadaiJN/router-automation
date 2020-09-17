from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(executable_path="F:\Drivers\chromedriver.exe")
browser.get("https://emulator.tp-link.com/EMULATOR_wr940nv6_eu_Router/userRpm/LoginRpm.htm")
browser.maximize_window()
#browser.find_element_by_name('username').send_keys('18751505')
browser.find_element_by_id('userName').send_keys('admin')
browser.find_element_by_id('pcPassword').send_keys('admin')
browser.find_element_by_id('loginBtn').click()
#browser.find_element_by_xpath('//button[text()="Entrar "]').click()
#browser.find_element_by_class_name('button').click()
