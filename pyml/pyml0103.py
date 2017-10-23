
#fboardlist > div.list-board > div.list-body > div:nth-child(1) > div > div > div > div.list-text > div.list-desc > a > strong

from bs4 import BeautifulSoup
import urllib.request as req

url = "https://www.kukudas.com/bbs/board.php?bo_table=JAV1A"
res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')

a_list = soup.select("#fboardlist > div.list-board > div.list-body > div > div > div > div > div.list-text > div.list-desc > a > strong")

for a in a_list:
    name = a.string
    print("-", name)