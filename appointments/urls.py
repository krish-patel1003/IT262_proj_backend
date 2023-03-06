from django.urls import path, include
from .views import appointmentsHome, SymptomViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('symptom', SymptomViewSet)

urlpatterns = [
    path("home/", appointmentsHome.as_view()),
    path(r'', include(router.urls))
]