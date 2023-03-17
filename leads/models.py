from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, pre_save
import datetime
class User(AbstractUser):
    is_organizor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
class LeadManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

class Lead(models.Model):
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    area_code = models.ForeignKey("AreaCode",on_delete=models.CASCADE,blank=True, null=True)
    phone = models.PositiveIntegerField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True,blank=False, null=True)
    converted_date = models.DateTimeField(blank=False, null=True)

    agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True, blank=True)
    organization = models.ForeignKey("UserProfile", on_delete=models.CASCADE, null=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='profile_picture', null=True, blank=True)

    # Module manager
    objects = LeadManager()

    def __str__(self):
        return f'{self.first_name}'

class AreaCode(models.Model):
     area_code = models.CharField(unique=True, max_length=4)
     country = models.CharField(max_length=20)

     def __str__(self):
         return self.area_code

def get_followup_folder_name(instance, filename):
    return f'followup/lead_{instance.lead.id}/{filename}'

class Manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter()
    
    def get_followups_date_order(self):
        return self.get_queryset().order_by('date_added')

class FollowUp(models.Model):
    lead = models.ForeignKey("Lead", related_name='followups' ,null=True, blank=True, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)
    my_file = models.FileField(null=True, blank=True,upload_to=get_followup_folder_name)
 
    def sorted_followups_set(self):
        return self.objects.all().order_by('date_added')

    def __str__(self):
        return f'{self.lead.first_name} {self.lead.last_name}'
    
def agent_folder_path(instance, filename):
    return f'agent_profiles/id_{instance.user.id}/{filename}'

class Agent(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE, related_name="agent")
    organization = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=agent_folder_path, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=15)
    organization = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    html_class = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
    

# Set organization for new user
def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
            # If user organizor
            if instance.is_organizor:
                # Create Organization Field
                UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)

# Set Agent User attributes for
def presave_agent_created_signal(sender, instance, **kwargs):
        instance.user.is_organizor = False
        instance.user.is_agent = True

pre_save.connect(presave_agent_created_signal, sender=Agent)

# Update Lead converted_date
def presave_set_lead_categor(sender, instance, **kwargs):
        converted_category = Category.objects.get(name='Converted')
        # SET default category if None
        if instance.category == None:
            # Take the default category
            empty_category = Category.objects.get(name='Empty')
            instance.category = empty_category  

        if instance.category == converted_category:
            instance.converted_date = datetime.datetime.now()
        
            
pre_save.connect(presave_set_lead_categor, sender=Lead)










