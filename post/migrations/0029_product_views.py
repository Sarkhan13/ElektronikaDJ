# Generated by Django 4.2.5 on 2023-10-15 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0028_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
