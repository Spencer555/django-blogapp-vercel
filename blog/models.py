from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse 

class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    