from django.db import models

# Create your models here.

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('apartment', 'Apartment'),
        ('home', 'Home'),
        ('land', 'Land'),
        ('suite', 'Suite'),
        ('shop', 'Shop'),
        ('mall', 'Mall'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=[('buy', 'Buy'), ('sell', 'Sell')])
    image = models.ImageField(upload_to='properties/')
    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Agent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='agents/')
    bio = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, null=True, blank=True)  # For font-awesome or similar icons

    def __str__(self):
        return self.title

