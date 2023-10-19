# Generated by Django 4.2.5 on 2023-10-17 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0038_remove_subuser_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='subuser',
            name='usertype',
            field=models.CharField(choices=[('Fərdi', 'Fərdi'), ('Mağaza', 'Mağaza'), ('Şirkət', 'Şirkət')], default=1, max_length=50, verbose_name='Istifadəçinin tipi'),
            preserve_default=False,
        ),
    ]
