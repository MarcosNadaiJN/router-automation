from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(executable_path="F:\Drivers\chromedriver.exe")
browser.get("https://studeo.unicesumar.edu.br/#!/access/login")
browser.maximize_window()
#browser.find_element_by_name('username').send_keys('18751505')
browser.find_element_by_id('username').send_keys('18751505')
browser.find_element_by_id('password').send_keys('4636894957229358')
browser.find_element_by_xpath('//button[text()="Entrar "]').click()
#browser.find_element_by_class_name('button').click()
