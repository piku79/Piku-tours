# Generated by Django 4.0.2 on 2022-05-08 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0010_remove_rate_num_starts_rate_num_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorite_travels',
            field=models.ManyToManyField(to='viewer.Travel'),
        ),
    ]
