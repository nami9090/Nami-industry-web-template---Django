# Generated by Django 5.2.2 on 2025-06-16 13:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_feature_icons'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='image_pic',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]
