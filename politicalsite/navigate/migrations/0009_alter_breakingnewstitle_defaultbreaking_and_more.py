# Generated by Django 4.1.3 on 2023-05-18 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigate', '0008_alter_aboutusbreadcumbarea_heading_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakingnewstitle',
            name='defaultbreaking',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='stockreport',
            name='currencyminusindex',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stockreport',
            name='currencyname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stockreport',
            name='currencyvalue',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='titles',
            name='defaultname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tricker',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]