import requests
from bs4 import BeautifulSoup

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색어를 입력해주세요: ")
url = base_url + keyword
req = requests.get(url)

html = req.text
soup = BeautifulSoup(html, "html.parser")

results = soup.select(".view_wrap") # select 검색해서 찾는 내용은 list와 동일한 데이터 구조를 갖는다.

count = 1
for i in results: # i <= .view_wrap
    title = i.select_one(".title_link").text
    link = i.select_one(".title_link")["href"]
    writer = i.select_one(".name").text
    dsc =  i.select_one(".dsc_link").text
    print(f"제목 : {title}")
    print(f"링크 : {link}")
    print(f"작성자 : {writer}")
    print(f"글요약 : {dsc}")
    print("------------")
    count += 1

print(count)