import BasePage

class SignInPage(BasePage):
  def __init__(self, driver):
    self.driver = driver
  
  def ClickCreateAccountButton(self):
     ClickButtonById("SubmitCreate")
     return CreateAccountPage(driver)

  def SetCreateAccountEmail(self, email):
    driver.find_element_by_id("email_create").clear()
    driver.find_element_by_id("email_create").send_keys(email)
    driver.find_element_by_id("email_create").send_keys(Keys.TAB) 