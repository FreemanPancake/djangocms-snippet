# Generated by Django 4.2.11 on 2024-05-07 03:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('djangocms_snippet', '0012_auto_20210915_0721'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site'),
        ),
    ]
