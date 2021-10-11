from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time
import re
driver = webdriver.Chrome('./chromedriver.exe')

driver.get("https://10minemail.com/en")
print(driver.title)
time.sleep(5)
email_element = driver.find_element_by_id("mail")
email = email_element.get_attribute('value')
print(email)
driver.execute_script("window.open('');")

driver.switch_to.window(driver.window_handles[1])
driver.get("https://sso2.agora.io/en/v4/signup/with-email?redirectUri=https%3A%2F%2Fconsole.agora.io")
inputEmail = driver.find_element_by_class_name("el-input__inner")
inputEmail.send_keys(email)
driver.find_element_by_class_name("el-checkbox__inner").click()
driver.find_element_by_xpath("//html/body/section/div[2]/div[2]/div[1]/div[1]/button").click()
driver.switch_to.window(driver.window_handles[0])
# driver.find_element_by_xpath("//html/body/section/div[2]/div[2]/div[1]/div[2]/button").click()
print('sleep start')
time.sleep(30)
print('sleep done')
WebDriverWait(driver, 15).until(lambda driver: driver.find_elements(By.XPATH,"//html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[3]/div[2]/a"))
driver.find_element_by_xpath("//html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[3]/div[2]/a").click()
time.sleep(5)
doc = driver.find_element_by_xpath('//html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]')
print(doc)
text = doc.get_attribute('innerHTML') 
verification = re.findall(r'[\d]{6}',text)
print(verification[0])
driver.switch_to.window(driver.window_handles[1])
inputVerification = driver.find_element_by_xpath("//html/body/section/div[2]/div[2]/div[1]/div[2]/div[3]/div/input")
inputVerification.send_keys(verification[0])
driver.find_element_by_xpath("//html/body/section/div[2]/div[2]/div[1]/div[2]/button").click()
WebDriverWait(driver, 15).until(lambda driver: driver.find_elements(By.XPATH,"//html/body/section/div[2]/div[1]/form/div[1]/div[1]/div/div/div[1]/input"))
firstName = driver.find_element_by_xpath('//html/body/section/div[2]/div[1]/form/div[1]/div[1]/div/div/div[1]/input')
firstName.send_keys("Phan")
lastName = driver.find_element_by_xpath('//html/body/section/div[2]/div[1]/form/div[1]/div[2]/div/div/div[1]/input')
lastName.send_keys("Trong")
companyName = driver.find_element_by_xpath('//html/body/section/div[2]/div[1]/form/div[2]/div/div[1]/input')
companyName.send_keys("GMO Runsystem")
passWord = driver.find_element_by_xpath('//html/body/section/div[2]/div[1]/form/div[4]/div/div[1]/input')
passWord.send_keys("Hahaha123@")
phoneNumber = driver.find_element_by_xpath('//html/body/section/div[2]/div[1]/form/div[3]/div/div[1]/input')
phoneNumber.send_keys("+84 94 629 51 23")
driver.find_element_by_xpath("//html/body/section/div[2]/div[1]/form/button").click()


# inputCheckBox.
assert "No results found." not in driver.page_source
driver.quit()

f = open("account.txt", "w")
f.writelines("account: " + email+"\n")
f.writelines("password: Hahaha123@")
f.close()
