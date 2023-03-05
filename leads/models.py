from django.db import models
from django.contrib.auth.models import AbstractUser



# class User(AbstractUser):
#     is_organisor = models.BooleanField(default=True)
#     is_agent = models.BooleanField(default=False)


class Lead(models.Model):
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(default=0, null=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return f'{self.first_name}'