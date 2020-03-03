# 유투브 동영상 다운로드

# 파이썬과 아나콘다 SSL 오류 날때 해결법

# 아나콘다가 설치된 G:\Anaconda3\Lib\site-packages\pip\_vendor\requests에 가서

# sessions.py를 메모장으로 열고

# 다음 python은 설치된 폴더 

# G:\Python38\Lib\site-packages\pip\_vendor\requests로 가서

# sessions.py를 메모장으로 열고 self.verify = False로 지정하면된다.

# 끝
# -*- conding: utf-8 -*-
import os
import subprocess

# pip install pytube3
import pytube


youtube_address = input("동영상주소는? (예시: https://www.youtube.com/watch?v=whBV&index=13)")
yt = pytube.YouTube(youtube_address) #다운받을 동영상 URL 지정

vids= yt.streams.all()





#영상 형식 리스트 확인
# for i in range(len(vids)):
#     print(i,'. ',vids[i])

#####################################동영상 형식 리스트 ##########################################################################################
# 0 .  <Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">
# 1 .  <Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">
# 2 .  <Stream: itag="136" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.4d401f" progressive="False" type="video">
# 3 .  <Stream: itag="247" mime_type="video/webm" res="720p" fps="30fps" vcodec="vp9" progressive="False" type="video">
# 4 .  <Stream: itag="135" mime_type="video/mp4" res="480p" fps="30fps" vcodec="avc1.4d4014" progressive="False" type="video">
# 5 .  <Stream: itag="244" mime_type="video/webm" res="480p" fps="30fps" vcodec="vp9" progressive="False" type="video">
# 6 .  <Stream: itag="134" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.4d401e" progressive="False" type="video">
# 7 .  <Stream: itag="243" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp9" progressive="False" type="video">
# 8 .  <Stream: itag="133" mime_type="video/mp4" res="240p" fps="30fps" vcodec="avc1.4d400c" progressive="False" type="video">
# 9 .  <Stream: itag="242" mime_type="video/webm" res="240p" fps="30fps" vcodec="vp9" progressive="False" type="video">
# 10 .  <Stream: itag="160" mime_type="video/mp4" res="144p" fps="30fps" vcodec="avc1.4d400b" progressive="False" type="video">
# 11 .  <Stream: itag="278" mime_type="video/webm" res="144p" fps="30fps" vcodec="vp9" progressive="False" type="video">
# 12 .  <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">
# 13 .  <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">

############################################################################################################################################
# vnum = int(input("다운 받을 화질은? "))

vids = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

download_folder = input("어디에다 저장? (예시: c:\\test) ")


#저장 폴더 생성(Windows or mac)
try:
    if not(os.path.isdir(download_folder)):
        os.makedirs(os.path.join(download_folder))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise


parent_dir = download_folder 

# 동영상 2번 형식(video/mp4" res="720p" fps="30fps) 다운로드 수행
vids.download(parent_dir) 

print('동영상 다운로드')





