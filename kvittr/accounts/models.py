from django.db import models

# Create your models here.

class UpdatePicture(models.Model):
	uname = models.CharField(max_length=30)
	user_picture = models.ImageField(upload_to='static/theme/user_images/', default='static/theme/images/675432109.jpg')
