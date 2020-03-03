
from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=rRzxEiBLQCA') # 유튜브 영상 URL 입력
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('g:\test') 