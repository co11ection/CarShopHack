from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from category.views import CategoryViewSet

router = DefaultRouter()
router.register('product', views.PostViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryViewSet.as_view()),
    path('comments/', views.CommentListCreateView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]