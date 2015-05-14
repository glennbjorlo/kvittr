from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.http import HttpResponse
from django.template import RequestContext

from kv_messages.models import Message

# Create your views here.

def message_listing(request):
	if request.method == 'POST':
		new_message = Message()
		new_message.uname = request.user
		new_message.umessage = request.POST.get('comment')
		new_message.created_datetime = timezone.now()
		new_message.save()
	kv_messages = Message.objects.all()
	context = {'kv_messages': kv_messages}
	return render(request, 'kv_messages/wall.html', context)


def message_details(request, message_id):
	kv_message = Message.objects.get(pk=message_id)
	context = {'kv_message': kv_message}
	return render(request, 'kv_messages/details.html', context)


#def create_new_message(request):
	
	
	
