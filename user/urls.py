from django.urls import include, path
from .views import signup, users, signin, AuthenticateUSer, signout
from rest_framework import routers


urlpatterns = [
    path('signup', signup),
    path('signin', signin),
    # path('users', users),
    path('currentuser', AuthenticateUSer.as_view()),
    path('signout', signout),
]