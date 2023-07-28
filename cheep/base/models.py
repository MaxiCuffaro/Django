from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField (max_length=199)
    text = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    def __str__(self):
        return f'{self.user.username}: {self.text}'
    
class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='mono.jpg')
    
    def __str__(self):
        return f'Perfil de {self.user.username}'
    
