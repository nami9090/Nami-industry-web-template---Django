# Generated by Django 5.2.2 on 2025-07-02 00:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_feature_iskingdom'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureBenefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iconStr', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=500)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='benefit', to='myapp.feature')),
            ],
        ),
    ]
