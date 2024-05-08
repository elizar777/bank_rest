from django.contrib import admin

# Register your models here.
from django.contrib import admin
from apps.transfer.models import HistoryTransfer
# Register your models here.

@admin.register(HistoryTransfer)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_user', 'to_user','is_completed', 'created_at', 'amount')