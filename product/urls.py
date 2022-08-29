from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from category.views import CategoryViewSet
from product.views import ProductViewSet
router = DefaultRouter()
router.register('product', views.ProductViewSet, basename='product')
urlpatterns = [
    path('', include(router.urls)),
    path('comments/', views.CommentListCreateView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]