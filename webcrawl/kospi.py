from urllib.request import urlopen
from bs4 import BeautifulSoup


url = 'https://finance.naver.com/sise/'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

res = soup.select('#KOSPI_now')
rs = [span.string for span in res]
for i in rs:
    print(i)

sel3 = soup.find_all('span', attrs={'class':'num num2'})
print(sel3)
sel = [span.strin for span in sel3]
for i in rs:
    print(" 코스피 :: {} , 코스닥 :: {} , 코스피 :: {}".format(soup.select('#KOSPI_now')[0].text
                                                            , soup.select('#KOSDAQ_now')[1].text
                                                            , soup.select('#KPI200_now')[2].text))