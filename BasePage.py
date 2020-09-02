from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

class BasePage(object):
  def __init__(self, driver, base_url=driver.current_url):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

  def ClickButtonByClass(className):
    driver.find_element_by_class_name(className).click()
  
  def ClickButtonById(id):
    driver.find_element_by_id(id).click()