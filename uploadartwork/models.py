from django.db import models
from django.contrib.auth.models import User

class ArtWork(models.Model):
    """ Model to add new artwork """

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    subject = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    width = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    depth = models.CharField(max_length=255)
    medium = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    styles = models.CharField(max_length=255)
    is_framed = models.BooleanField(default=False)
    is_copyright = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Images(models.Model):
    """ Images model for artwok """

    def get_user_image_folder(instance,filename):
        return "%s/%s" %('artwork/'+str(instance.post.id),filename)

    post = models.ForeignKey(ArtWork, on_delete=models.CASCADE,related_name='post')
    image = models.ImageField(upload_to=get_user_image_folder, verbose_name='Image')

    def __str__(self):
        return str(self.post)