from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Accesslogs(models.Model): 
    
    created_at = models.DateTimeField("접속 시간", auto_now_add=True)
    location = models.CharField("접속 경로", max_length=50)
