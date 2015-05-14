from django.conf.urls import patterns, url

from kv_messages import views

urlpatterns = patterns('',
	url(r'^$', views.message_listing, name='message_listing'),
	url(r'^$', views.create_new_message, name='create_new_message'),
	url(r'^(\d+)/$', views.message_details, name='message_details'),
)
