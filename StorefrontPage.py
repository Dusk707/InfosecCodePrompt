from BasePage import BasePage
from SignInPage import SignInPage

class StorefrontPage(BasePage):
  def __init__(self, driver):
    self.driver = driver

  def ClickSignInButton(self):
    BasePage.ClickButtonByClass(self, "login")
    return SignInPage(self.driver)

  def ClickSignOutButton(self):
    BasePage.ClickButtonByClass(self, "logout")