import BasePage

class CreateAccountPage(BasePage):
  def __init__(self, driver):
    self.driver = driver

  def ClearAddressLine1(self):
    driver.find_element_by_id("address1").clear()

  def ClearCity(self):
    driver.find_element_by_id("city").clear()

  def ClearCompany(self):
    driver.find_element_by_id("company").clear()

  def ClearInfoFirstName(self):
    driver.find_element_by_id("customer_firstname").clear()

  def ClearInfoLastName(self):
    driver.find_element_by_id("customer_lastname").clear()

  def ClearMobilePhone(self):
    driver.find_element_by_id("phone_mobile").clear()

  def ClearPassword(self):
    driver.find_element_by_id("passwd").clear()

  def ClearPostalCode(self):
    driver.find_element_by_id("postcode").clear()

  def ClickRegisterButton(self):
    ClickButtonById("submitAccount")
    return MyAccountPage(self.driver)

  def GetErrorMessageText(self):
    return driver.find_element_by_class_name("alert-danger").text

  def GetFieldValueById(self, id):
    return driver.find_element_by_id(id).get_attribute("value")

  def SetAddressLine1(self, address1):
    driver.find_element_by_id("address1").clear()
    driver.find_element_by_id("address1").send_keys(address1)
    driver.find_element_by_id("address1").send_keys(Keys.TAB)

  def SetCity(self, city):
    driver.find_element_by_id("city").clear()
    driver.find_element_by_id("city").send_keys(city)
    driver.find_element_by_id("city").send_keys(Keys.TAB)

  def SetCompany(self, company):
    driver.find_element_by_id("company").clear()
    driver.find_element_by_id("company").send_keys(company)
    driver.find_element_by_id("company").send_keys(Keys.TAB)

  def SetInfoFirstName(self, fName):
    driver.find_element_by_id("customer_firstname").clear()
    driver.find_element_by_id("customer_firstname").send_keys(fName)
    driver.find_element_by_id("customer_firstname").send_keys(Keys.TAB)

  def SetInfoLastName(self, lName):
    driver.find_element_by_id("customer_lastname").clear()
    driver.find_element_by_id("customer_lastname").send_keys(lName)
    driver.find_element_by_id("customer_lastname").send_keys(Keys.TAB)

  def SetMobilePhone(self, mPhone):
    driver.find_element_by_id("phone_mobile").clear()
    driver.find_element_by_id("phone_mobile").send_keys(mPhone)
    driver.find_element_by_id("phone_mobile").send_keys(Keys.TAB)

  def SetPassword(self, password):
    driver.find_element_by_id("passwd").clear()
    driver.find_element_by_id("passwd").send_keys(password)
    driver.find_element_by_id("passwd").send_keys(Keys.TAB)

  def SetPostalCode(self, postalCode):
    driver.find_element_by_id("postcode").clear()
    driver.find_element_by_id("postcode").send_keys(postalCode)
    driver.find_element_by_id("postcode").send_keys(Keys.TAB)

  def SetState(self, stateValue):
    driver.find_element_by_id("id_state").click()
    driver.find_element_by_xpath(f"//*[@id='id_state']/option[{stateValue}]").click()