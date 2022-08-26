from rest_framework import serializers
from .models import Product
from django.db.models import Avg
from .models import Favorites, Like, Comment


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price', 'images', 'user')
    
    def to_representation(self, instance):
        repr=super().to_representation(instance)
       
        repr['rating']= instance.reviews.aggregate(Avg('rating'))['rating__avg']
        return repr


class PrductDetailSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source ='user.email')
    class Meta:
        model = Product
        fields = '__all__'

    def is_liked(self, product):
        user = self.context.get('request').user
        return user.liked.filter(product=product).exists()
    
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        user = self.context.get('request').user
        if user.is_authenticated:
            repr['is_liked'] = self.is_liked(instance)
        repr['likes_count'] = instance.like.count()
        return repr

    
    


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('product',)
    
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['product'] = ProductListSerializer(instance.product).data
        return repr

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.email')

    class Meta:
        model = Like
        fields = ('user',)

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Comment
        fields = ('id', 'body', 'user', 'product')