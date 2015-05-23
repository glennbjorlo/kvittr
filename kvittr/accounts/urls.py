from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns('',
	url(r'^registration$', views.userregister, name='userregister'),
	url(r'^login$', views.userlogin, name='userlogin'),
	url(r'^logout$', views.userlogout, name='userlogout'),
	url(r'^settings$', views.updateprofile, name='updateprofile'),
)
