from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class ContainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Container
        fields = ['name', 'capacity']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'style', 'producer', 'abv']


class ProductContainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductContainer
        fields = ['product', 'container']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name']
