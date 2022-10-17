from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    image_thumbnail = ImageSpecField(source='image',
                                    processors=[ResizeToFill(100, 50)],
                                    format='JPEG',
                                    options={'quality': 60})