from django.contrib import admin
from .models import (
    Blog, BlogCategory,Property,
    Testimonial,Agent,Service,AgentApplication,ContactInfo, Message,Team,PropertyImage
)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('location', 'email', 'phone')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sent_at')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order')
    list_editable = ('display_order',)

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'location', 'featured')  # Fields to show in the admin list view
    list_filter = ('featured', 'location')  # Filters for the admin sidebar
    search_fields = ('title', 'address', 'location')  # Search functionality in admin

admin.site.register(Testimonial)
admin.site.register(Agent)
admin.site.register(Team)
admin.site.register(PropertyImage)

admin.site.register(AgentApplication)