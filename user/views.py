from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, status, renderers, viewsets, serializers
from rest_framework.decorators import api_view, renderer_classes

# Create your views here.


class UserViewSet(viewsets.ViewSet):
    
    def list(self, request):
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        user =User.objects.get(id=pk)
        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
