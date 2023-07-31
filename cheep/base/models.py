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
    
    def following(self):
        user_ids = Relationship.objects.filter(from_user=self.user)\
                                    .values_list('to_user_id', flat=True)
        
        return User.objects.filter(id__in=user_ids)
    
    def followers(self):
        user_ids = Relationship.objects.filter(to_user=self.user)\
                                    .values_list('from_user_id', flat=True)
        
        return User.objects.filter(id__in=user_ids)
    
   

class Relationship(models.Model):
    from_user = models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.from_user} to {self.to_user}'
    

class Hobbies(models.Model):
    name = models.CharField(max_length=50)
    desde_cuando = models.DateField()
    time_training =models.TimeField()

    def __str__(self):
        return f' Hobbies de {self.user.username}'