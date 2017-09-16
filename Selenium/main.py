# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
elem = driver.find_element_by_id("kw")
elem.send_keys("Python")
driver.find_element_by_id("su").click()
# elem.send_keys(Keys.RETURN)
print driver.page_source
