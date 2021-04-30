from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Категории')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length = 200, verbose_name = 'Название')
    price = models.DecimalField(max_digits = 7, decimal_places=0, verbose_name = 'Цена')
    count = models.IntegerField()
    avaliable = models.BooleanField(default = True)
    description = models.TextField(max_length = 1000, verbose_name = 'Описание')
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f"{self.name}"


class ProductImage(models.Model):
    product= models.ForeignKey(Product, related_name = 'photo', on_delete = models.CASCADE)
    photo = models.ImageField(upload_to='images', blank=True)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

 

