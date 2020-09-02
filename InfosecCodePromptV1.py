# This version is the first pass, where I flesh out exactly what I want the test to do
# It has limited extra functions and mainly directly uses the driver for webpage interaction

# installs (not needed in visual studio)
#!pip install selenium
#!apt-get update
#!apt install chromium-chromedriver
#!cp /usr/lib/chromium-browser/chromedriver /usr/bin

# set up driver
import sys
import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

# define commonly used functions
def HasElementById(id):
  elems = driver.find_elements_by_id(id)
  return len(elems) > 0

def HasElementByClass(className):
  elems = driver.find_elements_by_class_name(className)
  return len(elems) > 0

def Validation(condition, status, message):
  if status:
    if not condition:
      print(message)
  else:
    if condition:
      print(message)

def GetRandomString(length):
  letters = string.ascii_lowercase
  resultStr = ''.join(random.choice(letters) for i in range(length))
  return resultStr

def ClickButtonByClass(className):
  driver.find_element_by_class_name(className).click()

def ClickButtonById(id):
  driver.find_element_by_id(id).click()

# start test
# navigate to registration page to begin test
driver.get("http://automationpractice.com/index.php")
if HasElementByClass("logout"): # if an account is already logged in, log out
  driver.find_element_by_id("logout").click()
  driver.implicitly_wait(10)

driver.find_element_by_class_name("login").click()
driver.implicitly_wait(10)

print("Beginning step 1") # attempt to register without providing email
driver.find_element_by_id("SubmitCreate").click()
Validation(HasElementById("create_account_error"), True, "Error message not displayed")

print("Beginning step 2") # attempt to register with invalid email
emailField = driver.find_element_by_id("email_create")
emailField.clear()
emailField.send_keys("d;ifuagsdfhbasd")
emailField.send_keys(Keys.TAB)
Validation(HasElementByClass("form-error"), True, "Email field validation is not failing")
driver.find_element_by_id("SubmitCreate").click()
Validation(HasElementById("create_account_error"), True, "Error message not displayed")
    
print("Beginning step 3") # attempt to register with valid email
randString = GetRandomString(8)
email = f"test+{randString}@testing.com"
emailField.clear()
emailField.send_keys(email)
driver.find_element_by_id("SubmitCreate").click()
Validation(HasElementByClass("form-error"), False, "Email field validation is failing")
Validation(HasElementById("create_account_error"), False, "Error message is displayed")
autoFilledEmail = driver.find_element_by_id("email").get_attribute("value")
Validation(email == autoFilledEmail, True, "Auto filled email does not match provided email")
driver.implicitly_wait(10)
    
print("Beginning step 4") # attempt to register with no required fields entered
driver.find_element_by_id("submitAccount").click()
Validation(HasElementByClass("alert-danger"), True, "Error message is not displayed")
driver.implicitly_wait(10)
    
print("Beginning step 5") # attempt to register with some but not all required fields entered
driver.find_element_by_id("customer_firstname").clear()
driver.find_element_by_id("customer_firstname").send_keys("Bob")
driver.find_element_by_id("customer_lastname").clear()
driver.find_element_by_id("customer_lastname").send_keys("Billing")
driver.find_element_by_id("submitAccount").click()
Validation(HasElementByClass("alert-danger"), True, "Error message is not displayed")
driver.implicitly_wait(10)
    
print("Beginning step 6") # attempt to register with some non-required fields and no required fields entered
driver.find_element_by_id("company").clear()
driver.find_element_by_id("company").send_keys("Blue Tech")
driver.find_element_by_id("customer_firstname").clear()
driver.find_element_by_id("customer_lastname").clear()
driver.find_element_by_id("submitAccount").click()
Validation(HasElementByClass("alert-danger"), True, "Error message is not displayed")
driver.implicitly_wait(10)
    
print("Beginning step 7") # attempt to enter a number into first name field then click out of the field
driver.find_element_by_id("customer_firstname").clear()
driver.find_element_by_id("customer_firstname").send_keys("4")
driver.find_element_by_id("customer_firstname").send_keys(Keys.TAB)
Validation(HasElementByClass("form-error"), True, "Cusomter first name field validation is not failing")
driver.implicitly_wait(10)
    
print("Beginning step 8") # attempt to enter a string with special characters (/[](){}@&$) into first name field then click out of the field
driver.find_element_by_id("customer_firstname").clear()
driver.find_element_by_id("customer_firstname").send_keys("asda/[](){}@&$")
driver.find_element_by_id("customer_firstname").send_keys(Keys.TAB)
Validation(HasElementByClass("form-error"), True, "Cusomter first name field validation is not failing")
driver.implicitly_wait(10)
    
print("Beginning step 9") # attempt to enter a long string into first name field then click out of the field
driver.find_element_by_id("customer_firstname").clear()
driver.find_element_by_id("customer_firstname").send_keys(GetRandomString(50))
driver.find_element_by_id("customer_firstname").send_keys(Keys.TAB)
Validation(HasElementByClass("form-error"), True, "Cusomter first name field validation is not failing")
driver.implicitly_wait(10)
    
print("Beginning step 10") # attempt to enter a normal length string into first name field then click out of the field
driver.find_element_by_id("customer_firstname").clear()
driver.find_element_by_id("customer_firstname").send_keys("Bob")
driver.find_element_by_id("customer_firstname").send_keys(Keys.TAB)
Validation(HasElementByClass("form-error"), True, "Cusomter first name field validation is not failing")
driver.implicitly_wait(10)
autoFilledFirstName = driver.find_element_by_id("firstname").get_attribute("value")
Validation("Bob" == autoFilledFirstName, True, "Auto filled first name does not match provided first name")
    
print("Beginning step 11") # attempt to enter a string into the last name field
driver.find_element_by_id("customer_lastname").clear()
driver.find_element_by_id("customer_lastname").send_keys("Billings")
driver.implicitly_wait(10)
autoFilledLastName = driver.find_element_by_id("lastname").get_attribute("value")
Validation("Billings" == autoFilledLastName, True, "Auto filled last name does not match provided last name")
    
print("Beginning step 12") # attempt to enter a string of fewer than five characters into the password field then click out of the field
driver.find_element_by_id("passwd").clear()
driver.find_element_by_id("passwd").send_keys("1234")
driver.find_element_by_id("passwd").send_keys(Keys.TAB)
Validation(HasElementByClass("form-error"), True, "Password field validation is not failing")
driver.implicitly_wait(10)
    
print("Beginning step 13") # attempt to enter a string of five or more characters containing any of the above from 7-9 into the password field then click out of the field
driver.find_element_by_id("passwd").clear()
driver.find_element_by_id("passwd").send_keys("1234[]()")
driver.find_element_by_id("passwd").send_keys(Keys.TAB)
Validation(HasElementByClass("form-error"), False, "Password field validation is not failing")
driver.implicitly_wait(10)
    
print("Beginning step 14") # attempt to enter a non-mumeric string into the ZipCode and submit
driver.find_element_by_id("postcode").clear()
driver.find_element_by_id("postcode").send_keys("asdfg")
driver.find_element_by_id("submitAccount").click()
Validation(HasElementByClass("alert-danger"), True, "Error message is not displayed")
errorMessage = driver.find_element_by_class_name("alert-danger").text
Validation("Zip/Postal code" in errorMessage, True, "Error message is missing postal code error")
    
print("Beginning step 15") # attempt to enter a numeric string of under 5 characters and submit
driver.find_element_by_id("postcode").clear()
driver.find_element_by_id("postcode").send_keys("1234")
driver.find_element_by_id("submitAccount").click()
Validation(HasElementByClass("alert-danger"), True, "Error message is not displayed")
errorMessage = driver.find_element_by_class_name("alert-danger").text
Validation("Zip/Postal code" in errorMessage, True, "Error message is missing postal code error")
    
print("Beginning step 16") # attempt to enter a numeric string of over 5 characters and submit
driver.find_element_by_id("postcode").clear()
driver.find_element_by_id("postcode").send_keys("1234567")
driver.find_element_by_id("submitAccount").click()
Validation(HasElementByClass("alert-danger"), True, "Error message is not displayed")
errorMessage = driver.find_element_by_class_name("alert-danger").text
Validation("Zip/Postal code" in errorMessage, True, "Error message is missing postal code error")
    
print("Beginning step 17") # attempt to enter a numeric string of exactly 5 characters and submit
driver.find_element_by_id("postcode").clear()
driver.find_element_by_id("postcode").send_keys("12345")
driver.find_element_by_id("submitAccount").click()
Validation(HasElementByClass("alert-danger"), True, "Error message is not displayed")
errorMessage = driver.find_element_by_class_name("alert-danger").text
Validation("Zip/Postal code" in errorMessage, False, "Error message is displaying postal code error")
    
print("Beginning step 18") # attempt to enter a non-numeric string into the mobile phone number field and submit
driver.find_element_by_id("phone_mobile").clear()
driver.find_element_by_id("phone_mobile").send_keys("asdfg")
driver.find_element_by_id("submitAccount").click()
Validation(HasElementByClass("alert-danger"), True, "Error message is not displayed")
errorMessage = driver.find_element_by_class_name("alert-danger").text
Validation("phone_mobile" in errorMessage, True, "Error message is missing mobile phone error")
    
print("Beginning step 19") # attempt to enter a numeric string into the mobile phone number field and submit
driver.find_element_by_id("phone_mobile").clear()
driver.find_element_by_id("phone_mobile").send_keys("5555555555")
driver.find_element_by_id("submitAccount").click()
Validation(HasElementByClass("alert-danger"), True, "Error message is not displayed")
errorMessage = driver.find_element_by_class_name("alert-danger").text
Validation("phone_mobile" in errorMessage, False, "Error message is missing mobile phone error")
    
print("Beginning step 20") # attempt to complete form with all required fields properly filled in
driver.find_element_by_id("customer_firstname").clear()
driver.find_element_by_id("customer_firstname").send_keys("Bob")
driver.find_element_by_id("customer_lastname").clear()
driver.find_element_by_id("customer_lastname").send_keys("Billings")
driver.find_element_by_id("passwd").clear()
driver.find_element_by_id("passwd").send_keys("1234[]()")
driver.find_element_by_id("address1").clear()
driver.find_element_by_id("address1").send_keys("555 5th Street")
driver.find_element_by_id("postcode").clear()
driver.find_element_by_id("city").clear()
driver.find_element_by_id("city").send_keys("Fifth City")
driver.find_element_by_id("id_state").click()
driver.find_element_by_xpath("//*[@id='id_state']/option[7]").click()
driver.find_element_by_id("postcode").send_keys("12345")
driver.find_element_by_id("phone_mobile").clear()
driver.find_element_by_id("phone_mobile").send_keys("5555555555")
driver.find_element_by_id("submitAccount").click()
Validation(HasElementByClass("alert-danger"), False, "Error message is displayed")
Validation(HasElementByClass("info-account"), True, "Successful form submission did not go to expect account page")

# log out after successful run
driver.find_element_by_class_name("logout").click()