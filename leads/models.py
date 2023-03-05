from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_organizor = models.BooleanField(default=True)
    is_organizor = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    


class Lead(models.Model):
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(default=0, null=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return f'{self.first_name}'


class Agent(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE, related_name="agent")
    oraganization = models.ForeignKey("UserProfile", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    