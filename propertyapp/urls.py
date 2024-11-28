from django.urls import path

from . import views

app_name = 'propertyapp'

# Define the URL patterns for the student app
urlpatterns = [

    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('properties', views.properties, name='properties'),
    path('propertySingle', views.propertySingle, name='propertySingle'),
    path('services', views.services, name='services'),
    path('blog', views.blog, name='blog'),
    path('agent', views.agent, name='agent'),
     path('listing', views.listing, name='listing'),

]