from django.conf.urls import patterns, url

from kv_messages import views

urlpatterns = patterns('',
	url(r'^$', views.message_listing, name='message_listing'),
	url(r'^(\d+)/$', views.message_details, name='message_details'),
	url(r'^(\d+)/give_thumbs_up$', views.give_thumbs_up, name='give_thumbs_up'),
)
