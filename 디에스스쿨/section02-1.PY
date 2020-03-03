
#모듈 추가
import urllib.request

#인터넷 주소
url="https://subicura.com/assets/article_images/2017-01-19-docker-guide-for-beginners-1/docker-logo.png"
#저장파일 이름
savename="./img/docker_icon.png"

#이미지 저장
urllib.request.urlretrieve(url, savename)
