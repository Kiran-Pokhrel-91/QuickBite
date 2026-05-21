from django.db import models
from django.db.models import UniqueConstraint, Q

from apps.common.models import BaseModel
from apps.users.models import User
from apps.menu.models import MenuItem
from apps.resturants.models import Restaurant


class Cart(BaseModel):
    is_active = models.BooleanField(default=True, db_index=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='carts')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'restaurant'],
                condition=models.Q(is_active=True),
                name='unique_active_cart_per_user_restaurant'
            )
        ]
        indexes = [
            models.Index(fields=['user', 'is_active']),
        ]


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['cart', 'menu_item'],
                name='unique_cart_item'
            )
        ]
        indexes = [
            models.Index(fields=['cart']),
        ]