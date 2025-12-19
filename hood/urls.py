from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from . import views


# from django.urls import path, include

urlpatterns=[
    re_path('^$',views.welcome,name = 'welcome'),
    re_path('profile/',views.profile,name='profile'),
    re_path('update/',views.update_profile,name='update_profile'),
    re_path(r'^businesses',views.businesses, name='businesses'),
    re_path(r'^new/business$',views.new_business, name='new_business'),
    re_path(r'^search/', views.search_businesses, name='search_results'),
    re_path(r'^post/$', views.post, name='post'),
    re_path(r'^post/new/$', views.new_post, name='new_post'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)