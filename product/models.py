from django.db import models
from category.models import Category
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='products')
    title= models.CharField(max_length=100)
    year = models.CharField(max_length=30)
    color = models.CharField(max_length=100)
    mileage = models.CharField(max_length=100)
    engine= models.CharField(max_length=100)
    steering_wheel = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='products')
    images = models.ImageField(upload_to='images/', null = True, blank =True,)

    class Meta:
        ordering = ['title']

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user} -> {self.product} -> {self.created_at}'


class Like(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked')

    class Meta:
        unique_together = ['product', 'user']


class Favorites(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorites')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')

    class Meta:
        unique_together = ['product', 'user']

