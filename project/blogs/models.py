from django.db import models


# Create your models here.
class Aboutus(models.Model):
    title = models.CharField(max_length=800)
    chooseus = models.CharField(max_length=800)
    visionary = models.CharField(max_length=800)
    chooseus_img = models.ImageField(upload_to='about_images/')
    visionary_img = models.ImageField(upload_to='vison/')

    def __str__(self):
        return self.title


class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    subject = models.CharField(max_length=800)
    message = models.TextField()

    def __str__(self):
        return self.fullname


