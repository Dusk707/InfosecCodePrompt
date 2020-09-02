from BasePage import BasePage
from CreateAccountPage import CreateAccountPage
from selenium.webdriver.common.keys import Keys

class SignInPage(BasePage):
  def __init__(self, driver):
    self.driver = driver
  
  def ClickCreateAccountButton(self):
     BasePage.ClickButtonById(self, "SubmitCreate")
     return CreateAccountPage(self.driver)

  def SetCreateAccountEmail(self, email):
    self.driver.find_element_by_id("email_create").clear()
    self.driver.find_element_by_id("email_create").send_keys(email)
    self.driver.find_element_by_id("email_create").send_keys(Keys.TAB) 