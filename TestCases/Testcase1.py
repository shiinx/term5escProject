# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:29:11 2020

@author: psn99
"""

# Run through of the one customer with all agents available, input req details, connect, send message and end call

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

driver5 = webdriver.Chrome()
wait = WebDriverWait(driver5, 100)
driver5.get('https://web-sandbox.openrainbow.com/app/1.69.3/index.html')
wait.until(EC.presence_of_element_located((By.ID, "username")))
time.sleep(1)
username = driver5.find_element_by_id("username")
username.send_keys("testagent4@test.com")
time.sleep(2)
Continue = '/html/body/div[2]/authentication-component/authentication-window-component/div/div[1]/div[2]/div[2]/authentication-window-content/div/authentication-form-component/form/square-button/div/div'
wait.until(EC.element_to_be_clickable((By.XPATH, Continue)))
time.sleep(1)
driver5.find_element_by_xpath(Continue).click()
time.sleep(2)
pwd = driver5.find_element_by_id("authPwd")
pwd.send_keys("!2345Abcde")
Connect = "/html/body/div[2]/authentication-component/authentication-window-component/div/div[1]/div[2]/div[2]/authentication-window-content/div/authentication-form-component/form/square-button/div/div/span[2]"
wait.until(EC.element_to_be_clickable((By.XPATH, Connect)))
time.sleep(1)
driver5.find_element_by_xpath(Connect).click()
wait = WebDriverWait(driver5, 30)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "buttonTour")))
time.sleep(1)
driver5.find_element_by_class_name("buttonTour").click()
time.sleep(3)

driver = webdriver.Chrome()
driver.get('https://escproject.sutd.org/')
time.sleep(3)
# Click Live Chat
Live_Chat = '/html/body/div/div/button'
driver.find_element_by_xpath(Live_Chat).click()
# Input First Name
first_name = driver.find_element_by_xpath("/html/body/div/div/input[1]")
first_name.send_keys("Seyong1")
# Input Last Name
last_name = driver.find_element_by_xpath("/html/body/div/div/input[2]")
last_name.send_keys("Park1")
# Input Phone Number
phone_number = driver.find_element_by_xpath('/html/body/div/div/input[3]')
phone_number.send_keys("93976827")
# Please choose what you want to consult
select = Select(driver.find_element_by_xpath("/html/body/div/div/select"))
select.select_by_visible_text("Tablet")
time.sleep(3)
# Click Go Back
# Go_back = '/html/body/div/div[2]/button[2]'
# driver.find_element_by_xpath (Go_back).click()
# Click Start Chatting
Start_Chatting = '/html/body/div/div/button'
driver.find_element_by_xpath(Start_Chatting).click()
time.sleep(20)
chat = driver.find_element_by_xpath("/html/body/div/div/div[3]/textarea")
chat.send_keys("Hi My name is Seyong!")
time.sleep(2)
Send = "/html/body/div/div/div[3]/button"
driver.find_element_by_xpath(Send).click()
time.sleep(3)
chat = driver.find_element_by_xpath("/html/body/div/div/div[3]/textarea")
chat.send_keys("Help me!")
time.sleep(2)
Send = "/html/body/div/div/div[3]/button"
driver.find_element_by_xpath(Send).click()
time.sleep(3)
chat = driver.find_element_by_xpath("/html/body/div/div/div[3]/textarea")
chat.send_keys("Thank you for your help!")
time.sleep(2)
Send = "/html/body/div/div/div[3]/button"
driver.find_element_by_xpath(Send).click()
time.sleep(3)
endChat = "/html/body/div/div/div[1]/button"
driver.find_element_by_xpath(endChat).click()
time.sleep(3)

time.sleep(5)

driver.quit()

time.sleep(5)

driver5.quit()