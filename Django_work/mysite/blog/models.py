from django.conf import settings
from django.db import models
from django.utils import timezone

# db.sqlite3에 데이터베이스 생성
class Post(models.Model):
    # author = models.ForeignKey("auth.User", verbose_name=_("사용자"), on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # 데이터베이스 목록에 타이틀명을 보여주기
    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()


#### model를 생성했으면 반드시 python manage.py makemigrations -> python manage.py migrate를 실행해 줘야 된다.