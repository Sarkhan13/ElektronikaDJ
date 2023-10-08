# Generated by Django 4.2.5 on 2023-09-30 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='specialshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Bashliq')),
                ('subtitle', models.CharField(max_length=150, verbose_name='Alt bashliq')),
                ('link', models.TextField(verbose_name='url')),
                ('image', models.ImageField(upload_to='', verbose_name='bg_shekli')),
            ],
        ),
    ]