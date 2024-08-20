from django.db import models
import uuid
from django.contrib.auth.models import User

class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()

class  ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
    
    def __str__(self):
        return self.customer_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    