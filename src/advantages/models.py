from django.db import models

class Advantages(models.Model):
    icon  = models.ImageField(upload_to='uploads/')
    title = models.TextField(max_length=75)
    suptitle = models.TextField(max_length=255)