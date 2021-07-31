from rest_framework import routers

from .api import UserViewSet



router = routers.DefaultRouter()

router.register('api/account', UserViewSet, 'account')



urlpatterns = router.urls