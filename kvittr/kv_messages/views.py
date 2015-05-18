from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from kv_messages.models import Message

# Create your views here.

def message_listing(request):
	if request.method == 'POST':
		new_message = Message()
		new_message.uname = request.user
		new_message.umessage = request.POST.get('comment')
		new_message.created_datetime = timezone.now()
		new_message.save()
	kv_messages = Message.objects.all().order_by('-id')
	page_number = request.GET.get('page')
	paginator = Paginator(kv_messages, 5)
	try:
		kv_messages = paginator.page(page_number)
	except PageNotAnInteger:
		kv_messages = paginator.page(1)
	except EmptyPage:
		kv_messages = paginator.page(paginator.num_pages)
	context = {'kv_messages': kv_messages}
	return render(request, 'kv_messages/wall.html', context)


def message_details(request, message_id):
	kv_message = Message.objects.get(pk=message_id)
	context = {'kv_message': kv_message}
	return render(request, 'kv_messages/details.html', context)


def give_thumbs_up(request, message_id):
	kv_message = Message.objects.get(pk=message_id)
	kv_message.thumbs_up = kv_message.thumbs_up+1
	kv_message.save()
	data = {'thumbs_up': kv_message.thumbs_up}
	return JsonResponse(data)
	
	
	
