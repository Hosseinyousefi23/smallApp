from django.db import models
from django.utils import timezone


class Person(models.Model):
    # followers = models.ManyToManyField('self')
    # following = models.ManyToManyField('self')
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=100)
    sharif_mail_address = models.EmailField()
    profile_image = models.ImageField(upload_to='profile_image')

    def __str__(self):
        return self.name + " " + self.last_name


class Post(models.Model):
    is_public = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    context = models.TextField()
    publish_time = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100, default='unknown')

    def __str__(self):
        return self.author + " : " + self.title


