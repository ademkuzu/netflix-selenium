from selenium import webdriver
import time
url="https://www.netflix.com/tr/"
browser=webdriver.Firefox()
browser.get(url)
time.sleep(3)

login_link = browser.find_element_by_link_text("Oturum Aç")
login_link.click()
#time.sleep(10)
login=browser.find_element_by_name("userLoginId")
#your username
login.send_keys("**********")
parola=browser.find_element_by_id("id_password")
#your password
parola.send_keys("******")
time.sleep(3)

oturum_ac=browser.find_element_by_xpath("//*[@id='appMountPoint']/div/div[3]/div/div/div[1]/form/button")
oturum_ac.click()
time.sleep(10)



browser.close()

