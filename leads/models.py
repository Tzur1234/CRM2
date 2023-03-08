from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, pre_save

class User(AbstractUser):
    is_organizor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    


class Lead(models.Model):
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(default=0, null=True, blank=True)
    agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True, blank=True)
    organization = models.ForeignKey("UserProfile", on_delete=models.CASCADE, null=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return f'{self.first_name}'


class Agent(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE, related_name="agent")
    organization = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    icon = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=15)
    organization = models.ForeignKey("UserProfile", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
    

def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)


def post_agent_created_signal(sender, instance, created, **kwargs):
    if created:
        instance.user.is_organizor = False
        instance.user.is_agent = True

post_save.connect(post_agent_created_signal, sender=Agent)






