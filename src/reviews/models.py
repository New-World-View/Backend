from django.db import models

# Create your models here.
class Reviews(models.Model):
    username = models.TextField(max_length=110)
    message = models.TextField(max_length=355)
    created_at = models.DateTimeField(auto_now_add=True)