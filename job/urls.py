from django.urls import include, path
from .views import OfferViewSet, UserOfferViewSet, CvViewSet
from rest_framework import routers

urlpatterns = [
    path("offer" , OfferViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('offer/<str:pk>', OfferViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    path("useroffer" , UserOfferViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('useroffer/<str:pk>', UserOfferViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    path("cv" , CvViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('cv/<str:pk>', CvViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
]