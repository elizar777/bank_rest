from django.db import models

# Create your models here.
class Transfer(models.Model):
    from_user = models.CharField(
        max_length=255,
        verbose_name="Из токого пользователя"
    )
    to_user = models.CharField(
        max_length=255,
        verbose_name="На такого пользователя"
    )
    mount = models.CharField(
        max_length=255,
        verbose_name="Сколько денег помтупили"
    )