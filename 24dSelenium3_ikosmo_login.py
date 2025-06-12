# 셀레니움 모듈과 드라이버 임포트

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 웹드라이버 로드
driver = webdriver.Chrome()

# 네이버 메인에 접속
url = 'http://ikosmo.kr/main'
driver.get(url)

# XPath를 이용해서 네이버 메인의 '로그인' 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div/ul/li[1]/a').click()
# 로드와 상관없이 무조건 2초 대기
time.sleep(2)

# 로그인 페이지로 이동 후 아이디/비번의 입력상자를 찾은 후 정보 입력
driver.find_element(By.NAME, 'id').send_keys('parksh1632')
time.sleep(2)
driver.find_element(By.NAME, 'password').send_keys('conten11!')
time.sleep(2)

# 입력이 완려되면 '로그인' 버튼 클릭해서 로그인 시도
driver.find_element(By.XPATH, '//*[@id="subConts"]/div/div/div/div/section/section/form/fieldset/div[2]/ul/li/a').click
# 셀레니움 로그인을 감지하므로 캡챠 화면이 뜬다.
time.sleep(30)
# 조금 긴 시간을 대시하면서 직접 입력해준다.

driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div/a').click()
time.sleep(2)

# 검색 버튼을 눌러서 결과 확인
# driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/ul/li[2]/a/div').click()
# time.sleep(10)