from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import NoticeViewSet

router = SimpleRouter()
router.register('notification', NoticeViewSet)

urlpatterns = [
    path(r'', include(router.urls))
]