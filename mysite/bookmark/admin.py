from django.contrib import admin

# Register your models here.
#sy-added
from bookmark.models import Bookmark

#sy-added
#모델을 관리자 페이지에 등록
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'description', 'scope')