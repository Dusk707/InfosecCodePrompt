import BasePage

class MyAccountPage(BasePage):
  def __init__(self, driver):
    self.driver = driver

  def ClickLogOutButton(self):
    ClickButtonByClass("logout")