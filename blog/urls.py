from django.conf.urls import url, include
from . import views



urlpatterns = [
     url(r'^$', views.Blog.as_view(), name='blog'),
     url(r'^details/(?P<id>\d+)/$', views.blogdetail, name='blog-detail'),
   
]