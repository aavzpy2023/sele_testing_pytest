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

class TestTest1():
    def test_test1(self, driver):
        self.driver = driver
        self.driver.get("https://terp.versat.azcuba.cu/login")
        self.driver.set_window_size(1508, 848)
        self.driver.find_element(By.ID, "username-inputEl").send_keys("andrey")
        self.driver.find_element(By.ID, "password-inputEl").send_keys("A*123456")
        self.driver.find_element(By.ID, "aceptarButton-btnInnerEl").click()
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password-inputEl").send_keys("A*123456a")
        self.driver.find_element(By.ID, "aceptarButton-btnInnerEl").click()
        self.driver.find_element(By.CSS_SELECTOR, ".x-view-item-focused .erp-module-name").click()
        self.driver.find_element(By.ID, "ext-element-13").click()
        self.driver.find_element(By.ID, "inicioButton-btnEl").click()
        self.driver.find_element(By.CSS_SELECTOR, ".x-view-item-focused img").click()
        self.driver.find_element(By.ID, "ext-element-36").click()
        self.driver.find_element(By.ID, "inicioButton-btnInnerEl").click()
        self.driver.find_element(By.CSS_SELECTOR, ".x-view-item-focused > .erp-module-btn").click()
        self.driver.find_element(By.ID, "ext-element-41").click()
        self.driver.find_element(By.ID, "ext-element-42").click()
        self.driver.find_element(By.ID, "ext-element-48").click()
        self.driver.find_element(By.ID, "ext-element-64").click()
        self.driver.find_element(By.ID, "ext-element-66").click()
        self.driver.find_element(By.CSS_SELECTOR, "#checkcolumn-1541-textContainerEl .x-column-header-checkbox").click()
        self.driver.find_element(By.ID, "ext-element-66").click()
        self.driver.find_element(By.ID, "ext-element-68").click()
        self.driver.find_element(By.ID, "button-1021-btnWrap").click()
        self.driver.find_element(By.ID, "menuitem-1028-itemEl").click()
  
