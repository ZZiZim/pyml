
from bs4 import BeautifulSoup
import urllib.request as req

# Html 가져오기
url = "http://info.finance.naver.com/marketindex/"
res = req.urlopen(url)

# Html 분석
soup = BeautifulSoup(res, 'html.parser')

# 원하는 데이터 추출
price = soup.select_one("div.head_info > span.value").string
print("usd/krw=", price)