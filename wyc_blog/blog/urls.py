from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test/', views.Test, name="blog_test"),
    url(r'^post/(?P<id>\d+)/$', views.Detail, name="blog_detail"),
    url(r'^data_list/(?P<id>\d+)/$', views.Class_list, name="class_list"),
    url(r'^home/', views.home, name="blog_home"),
    url(r'^testpage/', views.testpage,),
    url(r'^add_article/', views.add_article),
    url(r'^add_classification/', views.classification),
]