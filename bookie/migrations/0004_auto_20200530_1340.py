# Generated by Django 3.0.6 on 2020-05-30 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookie', '0003_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(default='abc'),
        ),
    ]
