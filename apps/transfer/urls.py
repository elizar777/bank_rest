from rest_framework.routers import DefaultRouter

from apps.users.views import UserAPI

router = DefaultRouter()
router.register('transfer', UserAPI , "api_transfer")

urlpatterns = router.urls