# tweet/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 127.0.0.1:8000 과 views.py 폴더의 home 함수 연결
    path('tweet/', views.tweet, name='tweet'),  # 127.0.0.1:8000/tweet 과 views.py 폴더의 tweet 함수 연결
    path('tweet/delete/<int:id>', views.delete_tweet, name='delete-tweet'),
    path('tweet/<int:id>', views.detail_tweet, name='detail-tweet'),  # 해당 번호의 트윗과 댓글들을 읽어온다
    path('tweet/comment/<int:id>', views.write_comment, name='write-comment'),  # 해당 id 트윗에 댓글을 작성한다
    path('tweet/comment/delete/<int:id>', views.delete_comment, name='delete-comment'),  # 해당 댓글을 삭제한다
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
]
