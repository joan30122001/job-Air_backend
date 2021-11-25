from django.shortcuts import render
from .serializers import OfferSerializer, UserOfferSerializer, CvSerializer
from .models import Offer, UserOffer, Cv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, status, renderers, viewsets, serializers
from rest_framework.decorators import api_view, renderer_classes

# Create your views here.


class OfferViewSet(viewsets.ViewSet):
    
    def list(self, request):
        serializer = OfferSerializer(Offer.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        offer = Offer.objects.get(id=pk)
        serializer = OfferSerializer(offer)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = OfferSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        offer = Offer.objects.get(id=pk)
        serializer = OfferSerializer(instance=offer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        offer = Offer.objects.get(id=pk)
        offer.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)




class UserOfferViewSet(viewsets.ViewSet):
    
    def list(self, request):
        serializer = UserOfferSerializer(UserOffer.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        useroffer = UserOffer.objects.get(id=pk)
        serializer = UserOfferSerializer(useroffer)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = UserOfferSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        useroffer = UserOffer.objects.get(id=pk)
        serializer = UserOfferSerializer(instance=useroffer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        useroffer = UserOffer.objects.get(id=pk)
        useroffer.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)





class CvViewSet(viewsets.ViewSet):
    
    def list(self, request):
        serializer = CvSerializer(Cv.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        cv = Cv.objects.get(id=pk)
        serializer = CvSerializer(cv)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = CvSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        cv = Cv.objects.get(id=pk)
        serializer = CvSerializer(instance=cv, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        cv = Cv.objects.get(id=pk)
        cv.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)