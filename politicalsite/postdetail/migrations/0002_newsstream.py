# Generated by Django 4.1.3 on 2022-12-16 23:15

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('postdetail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsStream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', embed_video.fields.EmbedVideoField()),
                ('btn', models.CharField(max_length=30)),
                ('tag', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
