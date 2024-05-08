from rest_framework import serializers

from apps.transfer.models import HistoryTransfer

class HistoryTransferSerializer(serializers.ModelSerializer):
    # from_user_name = serializers.SerializerMethodField()
    # to_user_name = serializers.SerializerMethodField()

    class Meta:
        model = HistoryTransfer
        fields = ['id', 'from_user', 'to_user', 'is_completed', 'created_at', 'amount']
        # extra_kwargs = {
        #     'from_user': {'write_only': True},
        #     'to_user': {'write_only': True}
        # }

    # def get_from_user_name(self, obj):
    #     return obj.from_user.username

    # def get_to_user_name(self, obj):
    #     return obj.to_user.username