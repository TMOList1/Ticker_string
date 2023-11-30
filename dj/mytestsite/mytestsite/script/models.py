from django.db import models

class VideoRequest(models.Model):
	text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
