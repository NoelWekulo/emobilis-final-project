from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Property(models.Model):
    PROPERTY_TYPES = [
        ('buy', 'Buy'),  # Properties to buy
        ('sell', 'Sell'),  # Properties to sell
        ('listings', 'Listings'),  # General listings (organized by category)
    ]

    CATEGORIES = [
        ('land', 'Land'),
        ('apartment', 'Apartment'),
        ('home', 'Home'),
        ('mall', 'Mall'),
    ]
    
    

    title = models.CharField(max_length=200)
    description = models.TextField()
    long_description = models.TextField(blank=True, null=True)  # Detailed property description
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Optional for listings
    address = models.CharField(max_length=255, blank=True, null=True)  # Optional for certain categories
    location = models.CharField(max_length=100)
    bedrooms = models.IntegerField(blank=True, null=True)  # Optional for certain categories
    bathrooms = models.IntegerField(blank=True, null=True)  # Optional for certain categories
    image = models.ImageField(upload_to='properties/', default='properties/default.jpg')
    property_type = models.CharField(choices=PROPERTY_TYPES, max_length=10, default='Listings')
    
    category = models.CharField(choices=CATEGORIES, max_length=20, blank=True, null=True)  # Only used if type is 'listings'
    featured = models.BooleanField(default=False)  # Mark as featured
    agent_name = models.CharField(max_length=100, blank=True, null=True)  # Optional for listings
    agent_image = models.ImageField(upload_to='agents/', blank=True, null=True)  # Optional for listings
    agent_description = models.TextField(blank=True, null=True)  # Optional for listings
    twitter_url = models.CharField(max_length=55, blank=True, null=True)
    facebook_url = models.CharField(max_length=55, blank=True, null=True)
    linkedin_url = models.CharField(max_length=55, blank=True, null=True)
    instagram_url = models.CharField(max_length=55, blank=True, null=True)

    def __str__(self):
        return self.title


    

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')
    
    def __str__(self):
        return f"Property Image for {self.property.title}"
    
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



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default.jpg')

    def __str__(self):
        return f"{self.user.username}'s Profile"



