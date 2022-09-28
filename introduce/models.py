
from django.db import models

# Create your models here.
class Accesslogs(models.Model): 
    
    created_at = models.DateTimeField("접속 시간", auto_now_add=True)
    location = models.CharField("접속 경로", max_length=50)

    def __str__(self):
        #내가 쓰고 싶은 텍스트를 안에다가 넣어주면 된다f"{내가쓰고 싶은 텍스트}"
        return f"{self.created_at} / {self.location}"


