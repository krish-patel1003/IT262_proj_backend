from django.urls import path, include
from .views import (
    appointmentsHome, 
    SymptomViewSet, 
    AppointmentViewSet,
    PriscriptionViewSet
)
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('symptom', SymptomViewSet)
router.register('appointment', AppointmentViewSet)
router.register('prescription', PriscriptionViewSet)

urlpatterns = [
    path("home/", appointmentsHome.as_view()),
    path(r'', include(router.urls))
]