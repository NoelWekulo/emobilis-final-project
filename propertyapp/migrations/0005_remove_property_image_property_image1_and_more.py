# Generated by Django 5.1.2 on 2024-11-29 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertyapp', '0004_property_facebook_url_property_instagram_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='image',
        ),
        migrations.AddField(
            model_name='property',
            name='image1',
            field=models.ImageField(default='properties/default.jpg', upload_to='properties/'),
        ),
        migrations.AddField(
            model_name='property',
            name='image2',
            field=models.ImageField(default='properties/default.jpg', upload_to='properties/'),
        ),
        migrations.AddField(
            model_name='property',
            name='image3',
            field=models.ImageField(default='properties/default.jpg', upload_to='properties/'),
        ),
    ]