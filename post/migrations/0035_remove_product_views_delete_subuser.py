# Generated by Django 4.2.5 on 2023-10-17 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0034_subuser'),
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
