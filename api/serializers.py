from django.contrib.auth.models import User
from rest_framework import serializers

from myapp.models import ProductModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['url', 'name', 'price', 'desc', 'image', 'seller']
        
class AddProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    desc = serializers.CharField(required=True, max_length=100)
    price = serializers.IntegerField()
    #image = serializers.ImageField()
    
    def create(self, validated_data):
        """
        create and return a new "snippet" instance, given the validated data.
        """
        return ProductModel.objects.create(**validated_data)