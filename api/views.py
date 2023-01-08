from django.shortcuts import render
from myapp.models import ProductModel
# Create your views here.

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import  AddProductSerializer,UserSerializer,ProductSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ProductModel.objects.all().order_by('name')
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]
# Create your views here.
