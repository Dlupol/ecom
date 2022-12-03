from django.db import models
from django.urls import reverse


class Author(models.Model):

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    description = models.TextField()


class Category(models.Model):

    title = models.CharField(max_length=100)
    url = models.SlugField(max_length=160, unique=True)


class Product(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    draft = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)
    

class RatingStar(models.Model):

    value = models.SmallIntegerField(verbose_name='Значение', default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'
        ordering = ['-value']


class Rating(models.Model):

    ip = models.CharField(verbose_name='IP адрес', max_length=15)
    star = models.ForeignKey(RatingStar, verbose_name='звезда', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.PROTECT, related_name='ratings')

    def __str__(self):
        return f'{self.star} - {self.product}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Review(models.Model):

    name = models.CharField(verbose_name='Имя', max_length=100)
    text = models.TextField(verbose_name='Сообщение', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')
    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.PROTECT, related_name='reviews')

    def __str__(self):
        return f'{self.name} - {self.product}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'