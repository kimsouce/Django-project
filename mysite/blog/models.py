from django.db import models
from django.urls import reverse
#콘텐츠 편집
#from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils.text import slugify
from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    # 사용자를 foreignkey로 할당하기 위한 field 생성
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    tags = TaggableManager(blank=True)


    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering = ('-modify_dt',)

    #Post를 출력할 때 타이틀은 보여줌
    def __str__(self):
        return self.title

    #절대 주소 출력
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()

    #콘텐츠 출력
    #저장 시,  slug 자동 생성을 위한 메소드
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
