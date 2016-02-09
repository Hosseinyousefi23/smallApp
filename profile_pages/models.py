from django.db import models


class MySettings(models.Model):
    recieve_public = models.BooleanField()