from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class HistoryTransfer(models.Model):
    from_user = models.ForeignKey(
        User, related_name='transfers_sent', 
        on_delete=models.CASCADE, 
        verbose_name="От пользователя"
    )
    to_user = models.ForeignKey(
        User, 
        related_name='transfers_received', 
        on_delete=models.CASCADE, 
        verbose_name="К пользователю"
    )
    is_completed = models.BooleanField(
        default=False, 
        verbose_name="Перевод завершен"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата создания"
    )
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Сумма перевода"
    )

    def __str__(self):
        return f"Перевод от {self.from_user.username} к {self.to_user.username}"
    
    class Meta:
        verbose_name = "История перевода"
        verbose_name_plural = "История переводов"
