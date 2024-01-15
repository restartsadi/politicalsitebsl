# Generated by Django 4.1.3 on 2023-02-04 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigate', '0004_delete_commentbox'),
    ]

    operations = [
        migrations.CreateModel(
            name='CulturalNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p1', models.CharField(max_length=100)),
                ('p2', models.CharField(max_length=100)),
                ('p3', models.CharField(max_length=100)),
                ('imgthumb', models.ImageField(upload_to='pics')),
                ('ptext1', models.CharField(max_length=100)),
                ('ptext2', models.CharField(max_length=100)),
                ('blockqts', models.CharField(max_length=100)),
                ('singleptxt', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SportNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p1', models.CharField(max_length=100)),
                ('p2', models.CharField(max_length=100)),
                ('p3', models.CharField(max_length=100)),
                ('imgthumb', models.ImageField(upload_to='pics')),
                ('ptext1', models.CharField(max_length=100)),
                ('ptext2', models.CharField(max_length=100)),
                ('blockqts', models.CharField(max_length=100)),
                ('singleptxt', models.TextField(max_length=100)),
            ],
        ),
    ]
