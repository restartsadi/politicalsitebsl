# Generated by Django 4.1.3 on 2023-02-04 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postdetail', '0005_catagorygazettewelcomepostareaa_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditorialPostSingleSlide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('tag', models.CharField(max_length=20)),
                ('url', models.URLField(null=True)),
                ('headline', models.CharField(max_length=50)),
                ('headlineafterbr', models.CharField(max_length=150)),
                ('date', models.DateField(auto_now_add=True)),
                ('para', models.CharField(max_length=2000)),
            ],
        ),
    ]
