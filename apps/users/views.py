from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny


from apps.users.serializers import UserSerializer
from apps.users.models import User

class UserAPI(GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer