# Generated by Django 2.2.7 on 2021-05-09 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eMarket', '0004_category_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]
