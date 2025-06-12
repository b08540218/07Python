# 모듈 임포트
import requests
from bs4 import BeautifulSoup

'''
#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody
'''

# KBO 타자 기록실
response = requests.get("https://www.koreabaseball.com/Record/Player/HitterBasic/BasicOld.aspx?sort=HRA_RT")
# HTML 소스 저장
html = response.text
# Soup 객체로 변환
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# 타이틀 크롤링 : HTML태그 포함
title = soup.select_one('#contents > h4')
print("title 요소:",title)

# 태그를 제거하여 순수한 텍스트만 추출
title_txt = title.get_text()
print("title 요소:",title_txt)

# 타자기록이 있는 <table> 태그 전체를 얻어오기
record_table = soup.select_one('#cphContents_cphContents_cphContents_udpContent > div.record_result > table')
print("타자기록 요소 :", record_table)

# 타자 기록이 반복되어 출력되는  <tbody>를 얻어온 후 <tr>의 갯수만큼 반복
record_tr = soup.select_one('#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody')
repeat_tr = record_tr.select('tr')
for rec in repeat_tr:
  print("dddd", rec)

  d1 = rec.select_one('td:nth-child(1)').get_text()
  d2 = rec.select_one('td:nth-child(2)').get_text()
  d3 = rec.select_one('td:nth-child(3)').get_text()
  d4 = rec.select_one('td:nth-child(4)').get_text()
  d5 = rec.select_one('td:nth-child(5)').get_text()
  d6 = rec.select_one('td:nth-child(6)').get_text()
  d7 = rec.select_one('td:nth-child(7)').get_text()
  d8 = rec.select_one('td:nth-child(8)').get_text()
  d9 = rec.select_one('td:nth-child(9)').get_text()
  d10 = rec.select_one('td:nth-child(10)').get_text()
  
  d11 = rec.select_one('td:nth-child(11)').get_text()
  d12 = rec.select_one('td:nth-child(12)').get_text()
  d13 = rec.select_one('td:nth-child(13)').get_text()
  d14 = rec.select_one('td:nth-child(14)').get_text()
  d15 = rec.select_one('td:nth-child(15)').get_text()
  d16 = rec.select_one('td:nth-child(16)').get_text()
  d17 = rec.select_one('td:nth-child(17)').get_text()
  d18 = rec.select_one('td:nth-child(18)').get_text()
  d19 = rec.select_one('td:nth-child(19)').get_text()

  print(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19)





