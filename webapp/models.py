from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    creator=models.CharField(max_length=20,null=True)
    description=models.CharField(max_length=100)
    comments=models.CharField(max_length=50)

    
    def _str_(self):
        return self.creator

