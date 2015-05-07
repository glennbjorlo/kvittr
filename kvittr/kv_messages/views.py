from django.shortcuts import render

from kv_messages.models import Message

# Create your views here.

def message_listing(request):
	kv_messages = Message.objects.all();
	context = {'kv_messages': kv_messages}
	return render(request, 'kv_messages/wall.html', context)
