from django.urls import path, include

urlpatterns = [
    path('', include('minim.urls')),  # Map everything to the Minim application
]
