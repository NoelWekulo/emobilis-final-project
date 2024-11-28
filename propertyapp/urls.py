from django.urls import path

from . import views

app_name = 'propertyapp'

# Define the URL patterns for the student app
urlpatterns = [

    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('properties', views.properties, name='properties'),
    path('contact/', views.contact, name='contact'),
    path('propertySingle', views.propertySingle, name='propertySingle'),
    path('services', views.services, name='services'),
    path('blog', views.blog, name='blog'),
    path('agent', views.agent, name='agent'),
    path('listing', views.listing, name='listing'),
    path('buy', views.buy, name='buy'),
    path('sale', views.sale, name='sale'),
    path('blog/', views.blog_list, name='blog_list'),  # List all blogs
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('apply-agent/', views.apply_agent, name='apply_agent'),
    path('property/<int:pk>/', views.property_single, name='property_single'),


    path('blog/category/<slug:category_slug>/', views.blog_list, name='blog_by_category'),  # Filter blogs by category

]