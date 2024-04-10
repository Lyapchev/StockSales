from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StockViewSet, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'stocks', StockViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]