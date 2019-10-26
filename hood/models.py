from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Neighbourhood(models.Model):
    neighbourhood= models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.neighbourhood

    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls,neighbourhood):
        cls.objects.filter(neighbourhood=neighbourhood).delete()


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

class Bussiness(models.Model):
    title = models.CharField(max_length=30)
    bussiness_description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    address = models.TextField(max_length=60)
    

    def save_bussiness(self):
        self.save()
    
    @classmethod
    def get_all_bussiness(cls):
        bussiness= Bussiness.objects.all()
        return bussiness



        
