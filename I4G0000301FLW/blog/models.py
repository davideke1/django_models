from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    Title = models.CharField(max_length=200)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    Text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)