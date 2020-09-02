# set up driver
import sys
import unittest
import random
import string
from StorefrontPage import StorefrontPage
from SignInPage import SignInPage
from CreateAccountPage import CreateAccountPage
from MyAccountPage import MyAccountPage
#sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

# define commonly functions
def HasElementById(id):
  elems = driver.find_elements_by_id(id)
  return len(elems) > 0

def HasElementByClass(className):
  elems = driver.find_elements_by_class_name(className)
  return len(elems) > 0

# start test version 2, using page classes
# navigate to registration page to begin test
driver.get("http://automationpractice.com/index.php")
sfPage = StorefrontPage(driver)
if HasElementByClass("logout"): # if an account is already logged in, log out
  sfPage.ClickSignOutButton()
  driver.implicitly_wait(10)

signInPage = sfPage.ClickSignInButton()
driver.implicitly_wait(10)

print("Beginning step 1") # attempt to register without providing email
signInPage.ClickCreateAccountButton()
Validation(HasElementById("create_account_error"), True, "Error message not displayed")

print("Beginning step 2") # attempt to register with invalid email
signInPage.SetCreateAccountEmail("d;ifuagsdfhbasd")
Validation(HasElementByClass("form-error"), True, "Email field validation is not failing")
signInPage.ClickCreateAccountButton()
Validation(HasElementById("create_account_error"), True, "Error message not displayed")
    
print("Beginning step 3") # attempt to register with valid email
randString = GetRandomString(8)
email = f"test+{randString}@testing.com"
signInPage.SetCreateAccountEmail(email)
createAccountPage = signInPage.ClickCreateAccountButton()
Validation(HasElementByClass("form-error"), False, "Email field validation is failing")
Validation(HasElementById("create_account_error"), False, f"Error message is displayed")
autoFilledEmail = createAccountPage.GetFieldValueById("email")
Validation(email == autoFilledEmail, True, f"Auto filled email of {autoFilledEmail} does not match provided email of {email}")
driver.implicitly_wait(10)

print("Beginning step 4") # attempt to register with no required fields entered
createAccountPage.ClickRegisterButton()
Validation(HasElementByClass("alert-danger"), True, "Error message is not displayed")
driver.implicitly_wait(10)
    
print("Beginning step 5") # attempt to register with some but not all required fields entered
createAccountPage.SetInfoFirstName("Bob")
createAccountPage.SetInfoLastName("Billings")
createAccountPage.ClickRegisterButton()
Validation(HasElementByClass("alert-danger"), True, "Error message is not displayed")
driver.implicitly_wait(10)
    
print("Beginning step 6") # attempt to register with some non-required fields and no required fields entered
createAccountPage.SetCompany("Blue Tech")
createAccountPage.ClearInfoFirstName()
createAccountPage.ClearInfoLastName()
createAccountPage.ClickRegisterButton()
Validation(HasElementByClass("alert-danger"), True, "Error message is not displayed")
driver.implicitly_wait(10)
    
print("Beginning step 7") # attempt to enter a number into first name field then click out of the field
createAccountPage.SetInfoFirstName("4")
Validation(HasElementByClass("form-error"), True, "Cusomter first name field validation is not failing")
driver.implicitly_wait(10)
    
print("Beginning step 8") # attempt to enter a string with special characters (/[](){}@&$) into first name field then click out of the field
createAccountPage.SetInfoFirstName("asda/[](){}@&$")
Validation(HasElementByClass("form-error"), True, "Cusomter first name field validation is not failing")
driver.implicitly_wait(10)
    
print("Beginning step 9") # attempt to enter a long string into first name field then click out of the field
createAccountPage.SetInfoFirstName(GetRandomString(50))
Validation(HasElementByClass("form-error"), True, "Cusomter first name field validation is not failing")
driver.implicitly_wait(10)
    
print("Beginning step 10") # attempt to enter a normal length string into first name field then click out of the field
createAccountPage.SetInfoFirstName("Bob")
Validation(HasElementByClass("form-error"), True, "Cusomter first name field validation is not failing")
driver.implicitly_wait(10)
autoFilledFirstName = createAccountPage.GetFieldValueById("firstname")
Validation("Bob" == autoFilledFirstName, True, f"Auto filled first name {autoFilledFirstName} does not match provided first name Bob")
    
print("Beginning step 11") # attempt to enter a string into the last name field
createAccountPage.SetInfoLastName("Billings")
driver.implicitly_wait(10)
autoFilledLastName = createAccountPage.GetFieldValueById("lastname")
Validation("Billings" == autoFilledLastName, True, f"Auto filled last name {autoFilledLastName} does not match provided last name Billings")
    
print("Beginning step 12") # attempt to enter a string of fewer than five characters into the password field then click out of the field
createAccountPage.SetPassword("1234")
Validation(HasElementByClass("form-error"), True, "Password field validation is not failing")
driver.implicitly_wait(10)
    
print("Beginning step 13") # attempt to enter a string of five or more characters containing any of the above from 7-9 into the password field then click out of the field
createAccountPage.SetPassword("1234[]()")
Validation(HasElementByClass("form-error"), False, "Password field validation is not failing")
driver.implicitly_wait(10)
    
print("Beginning step 14") # attempt to enter a non-mumeric string into the ZipCode and submit
createAccountPage.SetPostalCode("asdfg")
createAccountPage.ClickRegisterButton()
Validation(HasElementByClass("alert-danger"), True, "Error message is not displayed")
errorMessage = createAccountPage.GetErrorMessageText()
Validation("Zip/Postal code" in errorMessage, True, f"Error message is missing postal code error: {errorMessage}")
    
print("Beginning step 15") # attempt to enter a numeric string of under 5 characters and submit
createAccountPage.SetPostalCode("1234")
createAccountPage.ClickRegisterButton()
Validation(HasElementByClass("alert-danger"), True, "Error message is not displayed")
errorMessage = createAccountPage.GetErrorMessageText()
Validation("Zip/Postal code" in errorMessage, True, f"Error message is missing postal code error: {errorMessage}")
    
print("Beginning step 16") # attempt to enter a numeric string of over 5 characters and submit
createAccountPage.SetPostalCode("1234567")
createAccountPage.ClickRegisterButton()
Validation(HasElementByClass("alert-danger"), True, "Error message is not displayed")
errorMessage = createAccountPage.GetErrorMessageText()
Validation("Zip/Postal code" in errorMessage, True, f"Error message is missing postal code error: {errorMessage}")
    
print("Beginning step 17") # attempt to enter a numeric string of exactly 5 characters and submit
createAccountPage.SetPostalCode("12345")
createAccountPage.ClickRegisterButton()
Validation(HasElementByClass("alert-danger"), True, "Error message is not displayed")
errorMessage = createAccountPage.GetErrorMessageText()
Validation("Zip/Postal code" in errorMessage, False, f"Error message is displaying postal code error: {errorMessage}")
    
print("Beginning step 18") # attempt to enter a non-numeric string into the mobile phone number field and submit
createAccountPage.SetMobilePhone("asdfg")
createAccountPage.ClickRegisterButton()
Validation(HasElementByClass("alert-danger"), True, "Error message is not displayed")
errorMessage = createAccountPage.GetErrorMessageText()
Validation("phone_mobile" in errorMessage, True, f"Error message is missing mobile phone error: {errorMessage}")
    
print("Beginning step 19") # attempt to enter a numeric string into the mobile phone number field and submit
createAccountPage.SetMobilePhone("5555555555")
createAccountPage.ClickRegisterButton()
Validation(HasElementByClass("alert-danger"), True, "Error message is not displayed")
errorMessage = createAccountPage.GetErrorMessageText()
Validation("phone_mobile" in errorMessage, False, f"Error message contains mobile phone error: {errorMessage}")
    
print("Beginning step 20") # attempt to complete form with all required fields properly filled in
createAccountPage.SetInfoFirstName("Bob")
createAccountPage.SetInfoLastName("Billings")
createAccountPage.SetPassword("1234[]()")
createAccountPage.SetAddressLine1("555 5th Street")
createAccountPage.SetCity("Fifth City")
createAccountPage.SetState(7)
createAccountPage.SetPostalCode("12345")
createAccountPage.SetMobilePhone("5555555555")
myAccountPage = createAccountPage.ClickRegisterButton()
Validation(HasElementByClass("alert-danger"), False, "Error message is displayed")
Validation(HasElementByClass("info-account"), True, "Successful form submission did not go to expect account page")

# logout for next run
myAccountPage.ClickLogOutButton()