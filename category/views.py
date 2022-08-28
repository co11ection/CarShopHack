from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from . import serializers
from .models import Category
from rest_framework import permissions
from rest_framework.decorators import action
# Create your views here.


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.CategoryListSerializer
        else:
            return serializers.CategoryDetailSerializer
    
    def get_permissions(self):
        if self.action in ('create', 'update','partial_update','destroy'):
            return [permissions.IsAdminUser]
        else:
            return [permissions.AllowAny]

