# Generated by Django 5.0.7 on 2024-07-30 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loop',
            name='bpm',
            field=models.IntegerField(default=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loop',
            name='categoria',
            field=models.CharField(default='Fm', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loop',
            name='escala',
            field=models.CharField(default='Trap', max_length=50),
            preserve_default=False,
        ),
    ]
