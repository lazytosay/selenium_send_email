from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

#purpose: use selenium to send email to someone else (not really useful, just a practice program)


from_email = 'test@gmail.com'
from_email_pass = 'testpassword'

to_email = ''
subject_msg = 'this an email sent by...'
body_msg = 'Hello world'

driver = webdriver.Chrome()

waitTime = WebDriverWait(driver, timeout=3)

#find the gmail button, click to go to the login page
driver.get('http://www.google.com')
elem = driver.find_element_by_id('gb_70')
elem.click()
try:
    #if it's not login page (shows a list of emails, and "other accout')
    elem = driver.find_element_by_id("identifierLink")
    elem.click()
except Exception as e:
    print("No other account button: ", e)
    elem = driver.find_element_by_xpath("//input[@id = 'identifierId']")
    print("It works")

#login in as usual
elem.send_keys(from_email)
elem.send_keys(Keys.RETURN)
waitTime.until(expected_conditions.visibility_of_element_located((By.NAME, "password"))).send_keys("thepassword" + Keys.RETURN)

#make sure everything is loaded
time.sleep(1)
driver.refresh()

driver.find_element_by_xpath("//a[@class='gb_P']").click()
driver.find_element_by_xpath("//div[@class='T-I J-J5-Ji T-I-KE L3']").click()
time.sleep(2)

try:
    #find the receiver box and enter to mail
    element = driver.find_element_by_xpath("//textarea[@id=':mr']")
    element.send_keys(to_email + Keys.ENTER)
    #find subject box and enter subject
    driver.find_element_by_xpath("//input[@name='subjectbox']").send_keys(subject_msg + Keys.ENTER)
    #find msg box and enter msg
    driver.find_element_by_xpath("//div[@id=':ne']").send_keys(body_msg)
except Exception as e:
    print("failed to enter the email address: ", e)
