from BasePage import BasePage

class StorefrontPage(BasePage):
  def __init__(self, driver):
    self.driver = driver

  def ClickSignInButton(self):
    BasePage.ClickButtonByClass("login")
    return SignInPage(driver)

  def ClickSignOutButton(self):
    BasePage.ClickButtonByClass("logout")