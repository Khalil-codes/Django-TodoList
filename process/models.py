from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField('Task Name:', max_length=40)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task
    
    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todo'