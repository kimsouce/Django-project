from django.urls import path, re_path
from blog import views

app_name = 'blog'
urlpatterns = [
    #Example: /blog/
    path('',views.PostLV.as_view(), name='index'),

    #Example: /blog/post/ (same as /blog/)
    path('post/', views.PostLV.as_view(), name='post_list'),

    #Example: /blog/post/django-example/
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),

    #Example: /blog/archive/
    path('archive/', views.PostAV.as_view(), name='post_archive'),

    #Example: /blog/archive/2020/
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),

    #Example: /blog/archive/2020/jun/
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),

    #Example: /blog/archive/2020/jun/03
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),

    #Example: search
    path('search/', views.SearchFormView.as_view(), name='search'),

    # 생성: http://127.0.0.1:8000/post/add/
    path('add/', views.PostCreateView.as_view(), name="add",),

    # 수정: http://127.0.0.1:8000/post/1/update/
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name="update",),

    # 삭제: http://127.0.0.1:8000/post/1/delete/
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name="delete",),

    #태그 기능 추가
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
]