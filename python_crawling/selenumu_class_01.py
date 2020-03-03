# 웹페이지 가져오기위한 웹드라이버 모듈
from selenium import webdriver

# 시간을 조절해서 웹페이지 가져오기 모듈 
from time import sleep


#크롬 드라이버 불러오기
driver = webdriver.Chrome("./chromedriver")

#웹페이지 주소
url ="https://www.fastcampus.co.kr/online_category/"

# try~except~finally 구문 시작
try:

    #웹페이지 가져오기
    driver.get(url)

    # 클래스 이름으로 여러문자를 불러올때 : element가 아니라 elements 복수형이어햐함
    # element인경우 'WebElement' object is not iterable error. 오류 발생
    courses = driver.find_elements_by_class_name('text_box')

    # 여러개 문자를 가져오기 위한 반복구문 
    for course in courses:
        print(course.text)

        # 1초 간격으로 해당문자 가져오기
        sleep(0.1)

except Exception as e:
    print(e)
# 웹페이지 가져오기 실패나 성공일때 최종 크롬드라이버 종료하기    
finally:
    driver.quit()