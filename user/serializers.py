from user.models import User
from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'pseudo',
            'email',
            'password',
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # retourner un dictionnaire
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        # retourner un dictionnaire
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance