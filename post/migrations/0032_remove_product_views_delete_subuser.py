# Generated by Django 4.2.5 on 2023-10-16 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0031_subuser_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='views',
        ),
        migrations.DeleteModel(
            name='subuser',
        ),
    ]
