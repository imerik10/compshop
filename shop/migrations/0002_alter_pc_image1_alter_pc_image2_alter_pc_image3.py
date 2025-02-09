# Generated by Django 4.2 on 2024-09-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pc',
            name='image1',
            field=models.ImageField(upload_to='media', verbose_name='1 картинка товара: '),
        ),
        migrations.AlterField(
            model_name='pc',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='2 картинка товара: '),
        ),
        migrations.AlterField(
            model_name='pc',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='3 картинка товара: '),
        ),
    ]
