from django.db import models
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категории')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    price = models.DecimalField(
        max_digits=7, decimal_places=0, verbose_name='Цена')
    count = models.IntegerField()

    avaliable = models.BooleanField(default = True)
    description = models.TextField(max_length = 1000, verbose_name = 'Описание')
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    booked = models.IntegerField(default = 0)
    sold = models.IntegerField(default = 0)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f"{self.name}"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name='photo', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images', blank=True)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

class Cart(models.Model):
    STATUS_CHOICES = (
        ('created', 'Created'), 
        ('progress', 'Progress'),
        ('finished', 'Finished'),
        ('canceled', 'Canceled') 
    ) 
    customer = models.CharField(max_length=30, verbose_name='владелец')
    number = models.CharField(max_length=20, verbose_name='номер владельца')
    created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, 
                              choices=STATUS_CHOICES, 
                              default='created')
    def __str__(self):
        return f"{self.customer}"
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

class CartProduct(models.Model):
    product = models.ForeignKey(Product, related_name='cart_product', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, related_name='cart_product', on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return f"{self.product}"

    class Meta:
        verbose_name = 'Продукт в корзине'
        verbose_name_plural = 'Продукты в корзине'
    
class Review(models.Model):
    customer_name = models.CharField(max_length=300, verbose_name='Имя')
    description = models.TextField(max_length = 1000, verbose_name='Описание')
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    created = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.customer_name}"
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
 
