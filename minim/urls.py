from django.urls import path, include
from rest_framework import routers

from minim import views

router = routers.DefaultRouter()
router.register(r'messages', views.MessageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
