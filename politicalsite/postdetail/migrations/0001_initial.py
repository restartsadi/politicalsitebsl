# Generated by Django 4.1.3 on 2022-12-16 19:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BreakingNewsWidget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('widget_title', models.CharField(max_length=50)),
                ('widgetimg', models.ImageField(upload_to='pics')),
                ('widgetbreakingnewstitle', models.CharField(max_length=100)),
                ('widgetheadline', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DetailPostHeading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SinglePostToday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_thumb_img', models.ImageField(upload_to='pics')),
                ('tag', models.CharField(max_length=30)),
                ('headline', models.CharField(max_length=100)),
                ('date', models.DateField(verbose_name=datetime.date)),
                ('comment', models.CharField(max_length=100)),
                ('para', models.CharField(max_length=5000)),
            ],
        ),
    ]
