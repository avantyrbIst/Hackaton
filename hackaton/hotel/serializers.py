from rest_framework import serializers
from .models import Login, Hotel
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User"""

    class Meta:
        model = User
        fields = ('id', 'username')


class LoginSerializer(serializers.ModelSerializer):
    """Сериализатор для профиля пользователя"""
    user = UserSerializer(read_only=True)

    class Meta:
        model = Login
        fields = ('id', 'user')

class HotelSerializer(serializers.ModelSerializer):
    """Сериализатор для категории"""
    posts = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'posts')