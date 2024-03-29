# Generated by Django 4.1.3 on 2023-05-29 09:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postdetail', '0007_singleteamarea_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='CulturalNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p1', models.CharField(max_length=1000)),
                ('p2', models.CharField(max_length=1000)),
                ('p3', models.CharField(max_length=1000)),
                ('imgthumb', models.ImageField(upload_to='pics')),
                ('ptext1', models.CharField(max_length=1000)),
                ('ptext2', models.CharField(max_length=1000)),
                ('blockqts', models.CharField(max_length=1000)),
                ('singleptxt', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='CulturalNewsArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('tag', models.CharField(max_length=1000)),
                ('url', models.URLField(null=True)),
                ('heading', models.CharField(max_length=1000)),
                ('date', models.DateField(verbose_name=datetime.date)),
            ],
        ),
    ]
