from django.urls import path, include
from .views import *
from users.student_views.views import ProfileViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

router = SimpleRouter()
router.register('profile', ProfileViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('home/', HomeView.as_view()),
    path(r'', include(router.urls), name="profile"),
]
