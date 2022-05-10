from rest_framework import serializers
from main.models import User, Book


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title','category', 'description', 'slug', 'image', 'price')
