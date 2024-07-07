from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test():
  driver = webdriver.Chrome()
  driver.implicitly_wait(3)
  driver.get('https://opensource-demo.orangehrmlive.com/')
  driver.maximize_window()
  
  # Login
  driver.find_element(By.NAME, 'username').send_keys('Admin')
  driver.find_element(By.NAME, 'password').send_keys('admin123')
  sleep(3)

  driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
  sleep(5)

  driver.quit()