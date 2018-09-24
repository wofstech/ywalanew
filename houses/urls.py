from django.conf.urls import url, include
from . import views
from django.contrib.auth.models import User


urlpatterns = [
    url(r'^addlisting/$', views.addlisting, name='addlisting'),
    url(r'^listing/details/(?P<id>\d+)/$', views.listbyuserdetails, name='detail'),
    url(r'^listing/details/(?P<pk>\d+)/editlist2$', views.editlist2, name='editlist2'),
    url(r'^listing/details/(?P<pk>\d+)/deletelist$', views.deletelist, name='deletelist'),
    url(r'^userlist/', views.UserListView.as_view(), name='userlist'),
    url(r'^alllisting/', views.alllisting.as_view(), name='alllisting'),
    url(r'^phone/(?P<id>\d+)$', views.phone, name='phone'),
    url(r'^vipsearch$', views.vipSearch, name='vipSearch'),
    url(r'^success/(?P<id>\d+)$', views.phone, name='phone'),
    url(r'^vipsearchuser/', views.VipListView.as_view(), name='viplist'),
   
    url(r'^vip/details/(?P<id>\d+)/$', views.vipbyuserdetails, name='vip-detail'),
    url(r'^vipdetails/(?P<pk>\d+)', views.deletelist2, name='deletelist2'),
    
   
]