# Generated by Django 4.2.5 on 2023-10-09 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0020_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]
