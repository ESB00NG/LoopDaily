# Generated by Django 5.0.7 on 2024-10-23 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loops', '0006_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='loop',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='loop_images/'),
        ),
    ]
