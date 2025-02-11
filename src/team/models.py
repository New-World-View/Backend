from django.db import models

# Create your models here.

class Team(models.Model):
    image = models.ImageField(upload_to='uploads/')
    username = models.TextField(max_length=150)
    profession = models.TextField(max_length=70)
    description = models.TextField(max_length=333)
    created_at = models.DateTimeField(auto_now_add=True)