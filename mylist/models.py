from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length= 512, verbose_name="Görev")
    is_completed = models.BooleanField(default=False, verbose_name="Tamamlandı mı?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
