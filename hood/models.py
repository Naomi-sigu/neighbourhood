from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
  profile_pic = models.ImageField(default='../static/images/default.jpeg',upload_to='media/')
  bio = models.TextField()
  user = models.OneToOneField(User,on_delete = models.CASCADE)
  
  @receiver(post_save , sender = User)
  def create_profile(instance,sender,created,**kwargs):
    if created:
      Profile.objects.create(user = instance)

  @receiver(post_save,sender = User)
  def save_profile(sender,instance,**kwargs):
    instance.profile.save()