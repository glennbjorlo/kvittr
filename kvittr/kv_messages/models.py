from django.db import models

# Create your models here.

class Message(models.Model):
	uname = models.CharField(max_length=30)
	umessage = models.TextField(max_length=140)
	thumbs_up = models.PositiveIntegerField(default=0)
	created_datetime = models.DateTimeField()
	def __unicode__(self):
		return u'%s (%s)' % (self.uname, self.umessage)
	
