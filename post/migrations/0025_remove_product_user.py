# Generated by Django 4.2.5 on 2023-10-11 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0024_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]
