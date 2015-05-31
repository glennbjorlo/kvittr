from django.db import models

# Create your models here.

class UpdatePicture(models.Model):
	uname = models.CharField(max_length=30)
	user_picture = models.ImageField(upload_to='theme/user_images/')
