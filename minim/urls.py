from django.urls import path, include
from rest_framework import routers

from minim import views

router = routers.DefaultRouter()
router.register(r'', views.MessageViewSet)

urlpatterns = [
    path('api/messages/', include(router.urls)),
]
