import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

#1~50 lst50 / 51~100 lst100
lst50 = soup.select(".lst50") # 1~50 list 형태로 들어가 있을거고 [1, 2, 3, 4, 5... 50]
lst100 = soup.select(".lst100")#51 ~ 100 list 형태로 들어가 있을거고 [51, 52, 53...100]
lst_all = lst50 + lst100 #lst50이랑 lst100을 합치고 싶어요 => 

for rank, i in enumerate(lst_all, 1):
    title = i.select_one(".ellipsis.rank01 a").text
    singer = i.select_one(".checkEllipsis").text
    album = i.select_one(".ellipsis.rank03 a").text

    print(f"[순위] : {rank}")
    print(f"[제목] : {title}")
    print(f"[가수] : {singer}")
    print(f"[앨범] : {album}")
    print()