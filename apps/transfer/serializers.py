from rest_framework import serializers
from apps.transfer.models import HistoryTransfer
from apps.users.serializers import UserSerializer

class HistoryTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryTransfer
        fields = ('id', 'from_user', 'to_user', 'is_completed', 'created_at', 'amount')
