from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'propertyapp'

# Define the URL patterns for the student app
urlpatterns = [

    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('properties', views.properties, name='properties'),
    path('contact/', views.contact, name='contact'), 
    path('property-single', views.propertysingle, name='property-single'),
    path('services', views.services, name='services'),
    path('blog', views.blog, name='blog'),
    path('agent', views.agent, name='agent'),
    path('buy/', views.buy_properties, name='buy_properties'),
    path('sell/', views.sell_property, name='sell_property'),
    path('listings/', views.listings, name='listings'),  # All listings
    path('listings/<str:category>/', views.listings, name='listings_by_category'),
    path('sell_success/', views.sell_success, name='sell_success'),
    
    
    path('blogs/', views.blog_list, name='blog_list'),  # List all blogs
    path('blogs/<slug:slug>/', views.blog_list, name='blog_list'),  # List all blogs
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('apply-agent/', views.apply_agent, name='apply_agent'),
    path('property/<int:pk>/', views.property_single, name='property_single'),
    path('Property/<int:pk>/', views.property_single, name='property_single'),
    path('property-single', views.property_single, name='property-single'),



    path('blog/category/<slug:category_slug>/', views.blog_list, name='blog_by_category'), 
      # Filter blogs by category
      # Authentication URLs
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),

    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
]