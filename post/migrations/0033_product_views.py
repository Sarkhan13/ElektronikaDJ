# Generated by Django 4.2.5 on 2023-10-16 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0032_remove_product_views_delete_subuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
