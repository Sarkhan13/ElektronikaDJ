# Generated by Django 4.2.5 on 2023-09-26 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
