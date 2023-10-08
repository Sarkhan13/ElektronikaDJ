# Generated by Django 4.2.5 on 2023-10-03 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0018_delete_notebook'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memory', models.IntegerField(verbose_name='Yaddaş')),
                ('ram', models.IntegerField(verbose_name='Operativ yaddaş')),
                ('color', models.CharField(choices=[('Ağ', 'Ağ'), ('Qara', 'Qara'), ('Mavi', 'Mavi')], max_length=100, verbose_name='Rəngi')),
                ('speed', models.FloatField(verbose_name='Suret(Ghz)')),
                ('processor', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.product', verbose_name='Məhsulun adı')),
            ],
        ),
    ]
