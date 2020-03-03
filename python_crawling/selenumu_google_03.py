# 웹페이지 가져오기위한 웹드라이버 모듈
from selenium import webdriver

# 시간을 조절해서 웹페이지 가져오기 모듈 
from time import sleep

# 웹검색 대상 구문 파싱
import urllib.request
import urllib.parse

from bs4 import BeautifulSoup

query = input("검색어: ")
page = input("검색페이지수: ")

#크롬 드라이버 불러오기
driver = webdriver.Chrome("./chromedriver")

#웹페이지 주소
url ="https://www.google.co.kr/search?"

values = {

  "q": query,  
  "sa":"N",
  "biw":"1680",
  "bih":"947"
  # "start":"40"
}


#1페이지 : https://www.google.co.kr/search?q=%EA%B5%AD%EB%A6%BD%EA%B3%B5%EC%9B%90&ei=AoA2XcjDL8mm0wTo0o_ABA&start=0&sa=N&ved=0ahUKEwjIzKnWjcrjAhVJ05QKHWjpA0gQ8tMDCLEB&biw=1680&bih=947
#2페이지 : https://www.google.co.kr/search?q=%EA%B5%AD%EB%A6%BD%EA%B3%B5%EC%9B%90&ei=AoA2XcjDL8mm0wTo0o_ABA&start=10&sa=N&ved=0ahUKEwjIzKnWjcrjAhVJ05QKHWjpA0gQ8tMDCLEB&biw=1680&bih=947
#3페이지 : https://www.google.co.kr/search?q=%EA%B5%AD%EB%A6%BD%EA%B3%B5%EC%9B%90&ei=pX82XYe0FsSzmAXb2JqgCg&start=20&sa=N&ved=0ahUKEwjHmuSpjcrjAhXEGaYKHVusBqQ4ChDy0wMIkQE&cshid=1563852819850940&biw=1680&bih=947
#4페이지 : https://www.google.co.kr/search?q=%EA%B5%AD%EB%A6%BD%EA%B3%B5%EC%9B%90&ei=3H82XbOrCtKLr7wP5OOMwAM&start=30&sa=N&ved=0ahUKEwizifXDjcrjAhXSxYsBHeQxAzg4FBDy0wMIew&biw=1680&bih=947

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
        
        webpages = driver.find_elements_by_class_name('rc')
       
        # i=1
        # 여러개 문자를 가져오기 위한 반복구문 
        for webpage in webpages:
            article = webpage.find_element_by_class_name('LC20lb')    
            address = webpage.find_element_by_class_name('iUh30')
            url = webpage.find_element_by_tag_name('a')
            href = url.get_attribute('href')

            html = urllib.request.urlopen(href)
            content = BeautifulSoup(html, "html.parser")               
              
                  
            # 번호와 글자출력시 개행문제 제거해서 한줄로
            print(str(i) + ". 기사제목: " + article.text.replace("\n", ""))
            print("링크주소: " + address.text.replace("\n", ""))
            print(href)
            print(content.body)
                                  
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