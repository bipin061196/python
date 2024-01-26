from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Server(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)    

    def __str__(self):
        return self.text
    
class Specification(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text[:50]}'
