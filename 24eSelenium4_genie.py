# 판다스, 셀레니움, 뷰티플숩 모듈 임포트
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# 크롬 웹 드라이버 로드 및 페이지 접속
driver = webdriver.Chrome()
url = 'https://www.genie.co.kr/chart/top200'
driver.get(url)

song_data =[]
rank = 1

# 1~4페이지까지 반복
for page in range(1,5):
  print("페이지", page)
  driver.implicitly_wait(2)

  # 파싱을 위해 페이지소스를 얻어온 후 Soup객체로 변환
  html = driver.page_source
  soup = BeautifulSoup(html, 'html.parser')

  # 각 챠트의 순위 반복을 위한 tr요소 선택
  songs = soup.select('tbody > tr')
  for song in songs:
    # 제목, 가수 등의 정보 파싱
    title = song.select('a.title')[0].text.strip()
    singer = song.select('a.artist')[0].text
    # 리스트에 추가
    song_data.append(['Genie', rank, title, singer])
    rank += 1
  if page < 4 :
    # 페이지 하단의 다음 순위 버튼을 클릭한다.
    # 버튼의 패턴은 a[1]~a[4]와 같다.
    driver.find_element(
      By.XPATH,
      f'//*[@id="body-content"]/div[7]/a[{page+1}]'
    ).click()
  driver.implicitly_wait(5)

# 리스트를 데이터프레임으로 변환 및 컬럼 추가
columns = ['서비스','순위','타이틀','가수']
pd_data = pd.DataFrame(song_data, columns=columns)
print(pd_data.head())
pd_data.to_excel('./saveFiles/genie_chart.xlsx', index=False)