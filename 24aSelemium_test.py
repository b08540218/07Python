from selenium import webdriver

driver = webdriver.Chrome()

import time
url = 'https://www.naver.com/'
driver.get(url)

time.sleep(5)