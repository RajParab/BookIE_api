# Generated by Django 3.0.6 on 2020-05-30 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookie', '0005_auto_20200530_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, default='True'),
        ),
    ]
