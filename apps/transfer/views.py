from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny


from apps.transfer.serializers import TransferSerializer
from apps.transfer.models import HistoryTransfer
# from apps.users.permission import UserPermissions
# Create your views here.

class UserAPI(GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = HistoryTransfer.objects.all()
    serializer_class = TransferSerializer