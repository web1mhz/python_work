# 웹페이지 가져오기위한 웹드라이버 모듈
from selenium import webdriver

# 시간을 조절해서 웹페이지 가져오기 모듈 
from time import sleep

# 웹검색 대상 구문 파싱
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

#태그 제거
import re

query = input("검색어: ")
page = input("검색페이지수: ")

#크롬 드라이버 불러오기
driver = webdriver.Chrome("./chromedriver")

#웹페이지 주소
url ="https://www.google.co.kr/search?"

values = {

  "q": query,
  "tbm":"nws",  
  "sa":"N",
  "biw":"1680",
  "bih":"898",
  "dpr":"1"
  # "start":"40"
}


# https://www.google.co.kr/search?q=%EA%B5%AD%EB%A6%BD%EA%B3%B5%EC%9B%90&tbm=nws&ei=i8U2XZocko-vvA_GyabIAQ&start=0&sa=N&ved=0ahUKEwjajZH-z8rjAhWSx4sBHcakCRk4ChDy0wMIUQ&biw=1680&bih=898&dpr=1

# https://www.google.co.kr/search?
# q=%EA%B5%AD%EB%A6%BD%EA%B3%B5%EC%9B%90
# &tbm=nws
# &ei=hsU2XZvzDYyJmAX7tpywDA
# &start=10
# &sa=N
# &ved=0ahUKEwibzu37z8rjAhWMBKYKHXsbB8YQ8tMDCFI
# &biw=1680
# &bih=898
# &dpr=1

params = urllib.parse.urlencode(values)

#print(params)

start = "&start="

api = url + params + start

# try~except~finally 구문 시작
try:

    i=1
    # 여러페이지 가져오기
    for st in range(0, int(page)* 10, 10):
        # print(st)

        #웹페이지 가져오기
        driver.get(api + str(st))
        # 클래스 이름으로 여러문자를 불러올때 : element가 아니라 elements 복수형이어햐함
        # element인경우 'WebElement' object is not iterable error. 오류 발생
        
        webpages = driver.find_elements_by_class_name('g')
       
        # i=1
        # 여러개 문자를 가져오기 위한 반복구문 
        for webpage in webpages:
            article = webpage.find_element_by_class_name('l.lLrAF')                
            url = webpage.find_element_by_tag_name('a')
            href = url.get_attribute('href')

            html = urllib.request.urlopen(href)
            content = BeautifulSoup(html, "html.parser")
            all_divs=str(content.find_all("div"))
            all_divs=re.sub('<.+?>', '', all_divs, 0).strip()               
              
                  
            # 번호와 글자출력시 개행문제 제거해서 한줄로
            print(str(i) + ". 기사제목: " + article.text.replace("\n", ""))
            print("링크주소: " + href.replace("\n", ""))
            
            print(all_divs)
                                  
            print("-"*100)

            # 1초 간격으로 해당문자 가져오기
            sleep(2)
            i+=1

    print("총 기사건수: " + str(i-1) + "건")


except Exception as e:
    print(e)

# 웹페이지 가져오기 실패나 성공일때 최종 크롬드라이버 종료하기    
finally:
    driver.quit()