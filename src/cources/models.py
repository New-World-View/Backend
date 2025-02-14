from django.db import models
from team.models import Team

class Cources(models.Model):
    image = models.ImageField(upload_to='uploads/')
    name_coursec = models.TextField(max_length=80)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.TextField(max_length=80)
    suptitle = models.TextField(max_length=320)
    info_course =  models.JSONField(default=list, blank=True)
    teachers = models.ManyToManyField(Team, related_name="courses")
    created_at = models.DateTimeField(auto_now_add=True)