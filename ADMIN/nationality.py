from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test():
  driver = webdriver.Chrome()
  driver.implicitly_wait(10)
  driver.get('https://opensource-demo.orangehrmlive.com/')
  driver.maximize_window()
  
  # Login
  driver.find_element(By.NAME, 'username').send_keys('Admin')
  driver.find_element(By.NAME, 'password').send_keys('admin123')
  sleep(3)

  driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
  sleep(4)

  # Click Admin Menu
  driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
  sleep(1.5)

  # Click Nationalities Menu
  driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a').click()
  sleep(1.5)

  # Click Add Nationality
  driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button').click()
  sleep(3.5)

  # Input Nationality Name
  driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input').send_keys('Test Nationality')
  sleep(2.3)

  # Click Save
  driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
  sleep(10)

  driver.quit()