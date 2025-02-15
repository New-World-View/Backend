from django.db import models
from teachers.models import Teachers

class Cources(models.Model):
    image = models.ImageField(upload_to='uploads/')
    name_coursec = models.TextField(max_length=80)  # Курс теперь привязывается к профессии учителей
    price = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.TextField(max_length=80)
    suptitle = models.TextField(max_length=320)
    info_course = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_teachers(self):
        """Получение всех учителей, у которых профессия совпадает с курсом"""
        return Teachers.objects.filter(profession=self.name_coursec)