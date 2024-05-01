from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(
        max_length=255, verbose_name= "Номер телефона"
    )
    age = models.CharField(
        max_length=3,
        verbose_name="Возраст"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )    
    password_confirm = models.CharField(
        max_length=2,
        verbose_name="Подтвердите пароль"
    )
    wallet_adress = models.CharField(
        max_length=6,
        verbose_name="ID кошелка"
    )
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"