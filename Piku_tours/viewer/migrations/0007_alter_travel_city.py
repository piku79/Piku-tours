# Generated by Django 4.0.2 on 2022-05-08 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0006_alter_travel_guide_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='viewer.city'),
        ),
    ]
