from django.db import models
#북마크 수정 및 삭제
from django.contrib.auth.models import User

# sy-added
#모델 지정
class Bookmark(models.Model):
    #타이틀 필드
    title = models.CharField('TITLE', max_length=100, blank=True)
    #url 필드
    url = models.URLField('URL', unique=True)
    #설명 필드
    description = models.CharField('DESCRIPTION', max_length=200, blank=True)
    #별점 필드
    scope = models.CharField('SCOPE', max_length=5, blank=True)
    #북마크 수정 및 삭제
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        #return "%s %s" %(self.title, "소연쓰의 보물상자")
        return self.title