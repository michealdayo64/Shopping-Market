# Generated by Django 2.2.7 on 2021-05-20 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eMarket', '0005_remove_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shipping_address',
        ),
    ]