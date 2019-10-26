from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


# from django.urls import path, include

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('profile/',views.profile,name='profile'),
]