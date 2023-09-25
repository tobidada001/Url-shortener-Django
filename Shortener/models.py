from django.db import models
import uuid
# Create your models here.

class ShortenedUrl(models.Model):
    url = models.URLField(max_length=1000)
    short_url = models.CharField(max_length = 8, default = str(uuid.uuid4())[:8], unique = True)
    scheme = models.CharField(max_length=5, default='http')
    
    def __str__(self):
        return self.short_url
