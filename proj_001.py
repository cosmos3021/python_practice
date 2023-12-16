import requests
from bs4 import BeautifulSoup

url = 'https://www.airkorea.or.kr/web/sidoAirInfo/sidoAirInfoDay01?itemCode=10008&ymd=2023-12-16%2010&areaCode=031&tDate=2023-12-01&monthDay=31'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

tags = soup.select('body > div > div > div.tblList.topFixScroll > table > tbody > tr:nth-of-type(7) > td:nth-of-type(1)')

tag = tags[0]
print('경기도 고양시 일산서구 주엽동의 미세먼지 농도는', tag.text.strip(), 'pm입니다')