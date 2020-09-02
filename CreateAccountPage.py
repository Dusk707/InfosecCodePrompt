from BasePage import BasePage
from MyAccountPage import MyAccountPage
from selenium.webdriver.common.keys import Keys

class CreateAccountPage(BasePage):
  def __init__(self, driver):
    self.driver = driver

  def ClearAddressLine1(self):
    self.driver.find_element_by_id("address1").clear()

  def ClearCity(self):
    self.driver.find_element_by_id("city").clear()

  def ClearCompany(self):
    self.driver.find_element_by_id("company").clear()

  def ClearInfoFirstName(self):
    self.driver.find_element_by_id("customer_firstname").clear()

  def ClearInfoLastName(self):
    self.driver.find_element_by_id("customer_lastname").clear()

  def ClearMobilePhone(self):
    self.driver.find_element_by_id("phone_mobile").clear()

  def ClearPassword(self):
    self.driver.find_element_by_id("passwd").clear()

  def ClearPostalCode(self):
    self.driver.find_element_by_id("postcode").clear()

  def ClickRegisterButton(self):
    BasePage.ClickButtonById(self, "submitAccount")
    return MyAccountPage(self.driver)

  def GetErrorMessageText(self):
    return self.driver.find_element_by_class_name("alert-danger").text

  def GetFieldValueById(self, id):
    return self.driver.find_element_by_id(id).get_attribute("value")

  def SetAddressLine1(self, address1):
    self.driver.find_element_by_id("address1").clear()
    self.driver.find_element_by_id("address1").send_keys(address1)
    self.driver.find_element_by_id("address1").send_keys(Keys.TAB)

  def SetCity(self, city):
    self.driver.find_element_by_id("city").clear()
    self.driver.find_element_by_id("city").send_keys(city)
    self.driver.find_element_by_id("city").send_keys(Keys.TAB)

  def SetCompany(self, company):
    self.driver.find_element_by_id("company").clear()
    self.driver.find_element_by_id("company").send_keys(company)
    self.driver.find_element_by_id("company").send_keys(Keys.TAB)

  def SetInfoFirstName(self, fName):
    self.driver.find_element_by_id("customer_firstname").clear()
    self.driver.find_element_by_id("customer_firstname").send_keys(fName)
    self.driver.find_element_by_id("customer_firstname").send_keys(Keys.TAB)

  def SetInfoLastName(self, lName):
    self.driver.find_element_by_id("customer_lastname").clear()
    self.driver.find_element_by_id("customer_lastname").send_keys(lName)
    self.driver.find_element_by_id("customer_lastname").send_keys(Keys.TAB)

  def SetMobilePhone(self, mPhone):
    self.driver.find_element_by_id("phone_mobile").clear()
    self.driver.find_element_by_id("phone_mobile").send_keys(mPhone)
    self.driver.find_element_by_id("phone_mobile").send_keys(Keys.TAB)

  def SetPassword(self, password):
    self.driver.find_element_by_id("passwd").clear()
    self.driver.find_element_by_id("passwd").send_keys(password)
    self.driver.find_element_by_id("passwd").send_keys(Keys.TAB)

  def SetPostalCode(self, postalCode):
    self.driver.find_element_by_id("postcode").clear()
    self.driver.find_element_by_id("postcode").send_keys(postalCode)
    self.driver.find_element_by_id("postcode").send_keys(Keys.TAB)

  def SetState(self, stateValue):
    self.driver.find_element_by_id("id_state").click()
    self.driver.find_element_by_xpath(f"//*[@id='id_state']/option[{stateValue}]").click()