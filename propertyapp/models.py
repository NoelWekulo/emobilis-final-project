from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# # class Property(models.Model):
#     PROPERTY_TYPE_CHOICES = [
#         ('apartment', 'Apartment'),
#         ('home', 'Home'),
#         ('land', 'Land'),
#         ('suite', 'Suite'),
#         ('shop', 'Shop'),
#         ('mall', 'Mall'),
#     ]
#     address = models.CharField(max_length=200)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     location = models.CharField(max_length=200)
#     icon = models.CharField(max_length=50) 
#     image = models.ImageField(upload_to='properties/')
#     property_type = models.CharField(max_length=50, choices=PROPERTY_TYPE_CHOICES)
#     status = models.CharField(max_length=20, choices=[('buy', 'Buy'), ('sell', 'Sell')])
#     created_at = models.DateTimeField(auto_now_add=True)
#     featured = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title


from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    image = models.ImageField(upload_to='properties/')
    featured = models.BooleanField(default=False)  # Mark as featured
    agent_name = models.CharField(max_length=100)
    agent_image = models.ImageField(upload_to='agents/')
    agent_description = models.TextField()
    twitter_url = models.CharField(max_length=55,blank=True,null=True)
    facebook_url = models.CharField(max_length=55,blank=True,null=True)
    linkedin_url = models.CharField(max_length=55,blank=True,null=True)
    instagram_url = models.CharField(max_length=55,blank=True,null=True)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    message = models.TextField()
    icon = models.CharField(max_length=50)
    rating = models.IntegerField(default=5) 
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Agent(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=15)
    image = models.ImageField(upload_to='agents/', default="profile.png")
    bio = models.TextField()
    twitter_url = models.CharField(max_length=55,blank=True,null=True)
    facebook_url = models.CharField(max_length=55,blank=True,null=True)
    linkedin_url = models.CharField(max_length=55,blank=True,null=True)
    instagram_url = models.CharField(max_length=55,blank=True,null=True)

    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=15)
    image = models.ImageField(upload_to='team/', default="profile.png")
    bio = models.TextField()
    twitter_url = models.CharField(max_length=55,blank=True,null=True)
    facebook_url = models.CharField(max_length=55,blank=True,null=True)
    linkedin_url = models.CharField(max_length=55,blank=True,null=True)
    instagram_url = models.CharField(max_length=55,blank=True,null=True)

    def __str__(self):
        return self.name

class ContactInfo(models.Model):
    location = models.TextField()
    open_hours = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"Contact Info"

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"



class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')  # Image field for service images
    read_more_url = models.URLField(null=True, blank=True, help_text="Optional URL for the 'Read More' link.")
    display_order = models.PositiveIntegerField(default=0, help_text="Order in which services are displayed.")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['display_order']
    

class BlogCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to Django's User model
    content = models.TextField()
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured_image = models.ImageField(upload_to='blogs/', null=True, blank=True)

    def __str__(self):
        return self.title
    


class AgentApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



