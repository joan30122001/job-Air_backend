from django.urls import include, path
from .views import UserViewSet
from rest_framework import routers


urlpatterns = [
    path("user" , UserViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    
]