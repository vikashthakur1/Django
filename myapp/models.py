from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField()
    mobile = models.CharField(max_length=15, )
    email = models.EmailField()

