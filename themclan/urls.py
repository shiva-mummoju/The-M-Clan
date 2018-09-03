from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.index, name='home'),
    url(r'^projects$', views.projects, name='projects'),
    url(r'^threedayevents$', views.threedayevent, name='threedayevents'),
    url(r'^about$', views.about, name='about'),
    url(r'^magazine$', views.magazine, name='magazine'),
    url(r'^pioneers$', views.pioneers, name='pioneer'),
]