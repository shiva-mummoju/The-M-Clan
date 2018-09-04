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
    
    url(r'^hpvc$', views.hpvc, name='hpvc'),
    url(r'^supra$', views.supra, name='supra'),
    url(r'^aero$', views.aero, name='aero'),
    url(r'^sdc$', views.sdc, name='sdc'),
    url(r'^baja$', views.baja, name='baja'),
]