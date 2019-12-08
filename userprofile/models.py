from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
    """ User Profile Model """

    about = models.TextField(blank=True)
    ex = models.TextField(blank=True)
    education = models.TextField(blank=True)
    address = models.CharField(max_length=250,blank=True)
    country = models.CharField(max_length=250,blank=True)
    city = models.CharField(max_length=250,blank=True)
    zip_or_postal_code = models.CharField(max_length=250,blank=True)
    phone = models.CharField(max_length=250,blank=True)
    image = models.ImageField(upload_to='profile_images/',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)