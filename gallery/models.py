from distutils.command.upload import upload
from email.mime import image
from django.db import models

# Create your models here.
class Picture(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pictures/')


    def __str__(self):
        return self.title