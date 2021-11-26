from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, status, renderers, viewsets, serializers
from rest_framework.decorators import api_view, renderer_classes
from .authentication import access_tokens, JwtAuthenticatedUser

# Create your views here.


@api_view(['post'])
def signup(request):
    data = request.data
    if data['password'] != data["password_confirm"]:
        raise exceptions.APIException("le mot de passe ne convient pas")
    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


# Methode signin
@api_view(['post'])
def signin(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed("user is not found ")
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed("incorret password")

    response = Response()
    # je genere le json web tken
    token = access_tokens(user)
    #  je set le cookie
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response

# j ' obtiens l 'authenticated user


class AuthenticateUSer(APIView):

    def get(self, request):
        data = UserSerializer(request.user).data
        #data['permissions'] = [p['name'] for p in data['role']['permissions']]
        return Response({
            'data': data
        })


@api_view(['post'])
def signout(request):
    response = Response()
    response.delete_cookie(key='jwt')
    response.data = {
        "detail": "success"
    }
    return response


@api_view(['GET'])
def users(request):
    serializer = UserSerializer(User.objects.all(), many=True)
    return Response(serializer.data)