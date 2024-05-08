from rest_framework.routers import DefaultRouter

from apps.transfer.views import TransferAPI

router = DefaultRouter()
router.register('transfer', TransferAPI , "api_transfer")

urlpatterns = router.urls