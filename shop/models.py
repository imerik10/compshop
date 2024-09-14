from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=250,verbose_name='Название категории: ')
    slug = models.SlugField(verbose_name='Слэг категории: ',max_length=255,)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.category_name
    

class PC(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=255,verbose_name='Товар:')
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Цена: ')
    description = models.TextField(verbose_name='Описание: ')
    image1 = models.ImageField(upload_to='media',verbose_name='1 картинка товара: ')
    image2 = models.ImageField(upload_to='media',blank=True, null=True,verbose_name='2 картинка товара: ')
    image3 = models.ImageField(upload_to='media',blank=True, null=True,verbose_name='3 картинка товара: ')

    class Meta:
        verbose_name = 'Tovar'
        verbose_name_plural = 'Tovarlar'

    def __str__(self):
        return self.name