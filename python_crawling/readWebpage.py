# 모듈 추가
import urllib.request

# 웹페이지 주소
url="http://www.naver.com"

# 웹페이지 읽어오기
data= urllib.request.urlopen(url).read()

# 화면 출력
print(data.decode("utf-8"))
print("\n")
