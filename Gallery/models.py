from django.conf import settings
from django.db import models
from django.utils import timezone


class Img_Files(models.Model):
    img = models.FileField(upload_to='Gallery/users_images')
    
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    posted_imgs = models.ManyToManyField(Img_Files, blank=True)

    def __str__(self):
        return self.title
    