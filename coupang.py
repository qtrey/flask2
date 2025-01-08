from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

header_user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

options_ = Options() #인스턴스화
options_.add_argument(f"User-Agent={header_user}") # 유저 정보 넣기
options_.add_experimental_option("detach", True) #자동으로 브라우저가 종료되지 않게
options_.add_experimental_option("excludeSwitches",["enable-logging"])

driver = webdriver.Chrome(options=options_)

keyword = input("검색할 상품 : ")
url = f"https://www.coupang.com/np/search?component=&q={keyword}"

driver.get(url) #chrome 브라우저 = driver

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".search-product-wrap.adjust-spacing")
print(len(items))

# 검색순위 1위부터 10위까지만 나오게하고 광고 제품은 제외해주세요
# 1. 광고 제품인지 아닌지를 구분한다
# 2. 출력 결과에서 1위부터 10까지만을 출력하도록 조건을 만든다
# 순위?? html 코드에서 추출도 가능하겠지만, 변수 또는 enumerate 사용할 수 있다고 배웠다.

for rank, i in enumerate(items, 1):
    ad = i.select_one(".ad-badge-text") #<span class="ad-badge-text">  AD  </span>
    print(type(ad))
    if not ad: #ad에 값이 있어 => true , not -> 부정을해 -> None -> false -> true
        product_name = i.select_one(".name").text
        product_price = ""
        link = "" #링크 가져오기 naver에서 했어요
        roket = "" #로켓배송인지 아닌지에 대한 여부를 알려주는 코드를 작성해주세요
        # 1위부터 10위까지 나오도록        
        print(f"제품명 : {product_name}")

# driver.quit()