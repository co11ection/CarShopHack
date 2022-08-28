from django.db import models
from django.contrib.auth import get_user_model
from account.models import UserManager
from product.models import Product
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
# Create your models here.

User = get_user_model()

STATUS_CHOISES = (
    ('open', 'Открыт'), 
    ('in_process', 'в обработке'), 
    ('closed', 'Закрыт')
    )

class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.SmallIntegerField(default=1)



class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders',on_delete=models.RESTRICT )
    product=models.ManyToManyField(Product, through=OrderItem,)
    status = models.CharField(max_length=20, choices=STATUS_CHOISES)
    cteated_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



    

