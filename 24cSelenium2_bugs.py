# 셀레니움에서 웹드라이버 임포트
from selenium import webdriver
# 크롬 드라이버 로드. 이떄 웹브라우저가 실행됨
from bs4 import BeautifulSoup
driver = webdriver.Chrome()


driver.implicitly_wait(5)

# import time
# time.sleep(5)

# 셀레니움을 통해 접속한 후 페이지의 정보(HTML소스)를 얻어옴
url = 'https://music.bugs.co.kr/chart'
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


# 뷰티플숩을 입포트 한 후 얻어온 정보를 Soup객체로 변환


song_data = []
ranking = 1
songs = soup.select('tbody > tr')
for song in songs:
  # 순위
  ranking = song.select('tr:nth-child(1) > td:nth-child(4)') [0].text
  # 곡
  #CHARTrealtime > table > tbody > tr:nth-child(1) > th
  title = song.select('tr:nth-child(1) > th') [0].text
  # 아티스트
  #CHARTrealtime > table > tbody > tr:nth-child(1) > td:nth-child(8) > p > a
  art = song.select('tr:nth-child(1) > td:nth-child(8) > p > a') [0].text
  # 앨범
  #CHARTrealtime > table > tbody > tr:nth-child(1) > td:nth-child(9) > a
  album = song.select('tr:nth-child(1) > td:nth-child(9) > a') [0].text

  print(title, art, album, sep="|")
  song_data.append({'Melon', ranking, title, art, album})
  ranking += 1
  import pandas as pd
  columns = ['순위', '곡', '아티스트', '앨범']
  pd_data = pd.DataFrame(song_data, columns=columns)
  print(pd_data.head())
  pd_data.to_excel('./saveFiles/bugs_Chart.', index=False)
