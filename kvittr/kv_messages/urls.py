from django.conf.urls import patterns, url

from kv_messages import views

urlpatterns = patterns('',
	url(r'^$', views.message_listing, name='message_listing'),
)
