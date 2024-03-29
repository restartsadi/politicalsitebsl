# Generated by Django 4.1.3 on 2022-12-19 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postdetail', '0003_gazettectaarea'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleTeamArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=30)),
                ('sociallinks', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('href', models.URLField(max_length=100)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TeamArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=30)),
            ],
        ),
    ]
