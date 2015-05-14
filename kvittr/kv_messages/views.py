from django.shortcuts import render
from django.utils import timezone

from kv_messages.models import Message

# Create your views here.

def message_listing(request):
	kv_messages = Message.objects.all()
	context = {'kv_messages': kv_messages}
	return render(request, 'kv_messages/wall.html', context)


def message_details(request, message_id):
	kv_message = Message.objects.get(pk=message_id)
	context = {'kv_message': kv_message}
	return render(request, 'kv_messages/details.html', context)


def create_new_message(request):
	if request.method == "POST":
		message = Message()
		message.uname = request.user
		message.umessage = request.POST.get('comment')
		message.created_datetime = timezone.now()
		message.save()
	return render(request, 'kv_messages/wall.html')
	
	
