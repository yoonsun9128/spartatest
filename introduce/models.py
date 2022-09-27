from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Accesslogs(models.Model): 
    class Meta:
        db_table = "my_user"
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=20, null=False)
