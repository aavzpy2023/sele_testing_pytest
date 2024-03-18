# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestT1():
    def test_t1(self, driver):
        self.driver = driver
        # Test name: t1
        # Step # | name | target | value
        # 1 | open | https://opensource-demo.orangehrmlive.com/web/index.php/auth/login | 
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # 2 | type | name=username | Admin
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        # 3 | type | name=password | admin123
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        # 4 | click | css=.oxd-button | 
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        # 5 | click | linkText=Admin | 
        self.driver.find_element(By.LINK_TEXT, "Admin").click()
        # 6 | click | css=.oxd-button--secondary:nth-child(1) | 
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--secondary:nth-child(1)").click()
        # 7 | click | css=.oxd-select-text--focus > .oxd-select-text-input | 
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-select-text--focus > .oxd-select-text-input").click()
        # 8 | mouseUp | css=.oxd-grid-item:nth-child(3) | 
        element = self.driver.find_element(By.CSS_SELECTOR, ".oxd-grid-item:nth-child(3)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        # 9 | click | css=.oxd-table-card:nth-child(5) .oxd-table-cell:nth-child(2) > div | 
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-table-card:nth-child(5) .oxd-table-cell:nth-child(2) > div").click()
        # 10 | click | css=.oxd-table-card:nth-child(5) .oxd-table-cell:nth-child(2) > div | 
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-table-card:nth-child(5) .oxd-table-cell:nth-child(2) > div").click()
        # 11 | click | css=.oxd-userdropdown-icon | 
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-icon").click()
        # 12 | click | linkText=Logout | 
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
  
