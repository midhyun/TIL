from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length = 40)
    script = models.TextField()
    start_date = models.DateField(auto_now_add = True)
    end_date = models.DateField(auto_now_add = True)
    completed = models.BooleanField(default = False)