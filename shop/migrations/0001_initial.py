# Generated by Django 4.2 on 2024-09-12 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=250, verbose_name='Название категории: ')),
                ('slug', models.SlugField(max_length=255, verbose_name='Слэг категории: ')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='PC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Товар:')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена: ')),
                ('description', models.TextField(verbose_name='Описание: ')),
                ('image1', models.ImageField(upload_to='', verbose_name='1 картинка товара: ')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='2 картинка товара: ')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='3 картинка товара: ')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
            options={
                'verbose_name': 'Tovar',
                'verbose_name_plural': 'Tovarlar',
            },
        ),
    ]
