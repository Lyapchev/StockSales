from rest_framework import viewsets
from .models import Stock, Post, Comment
from.serializers import StockSerializer, PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class StockViewSet(viewsets.ModelViewSet):
    #queryset = Stock.objects.get_queryset().order_by('-id')
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #filter_backends = [DjangoFilter]
    
    #permission_classes = [IsAuthenticatedOrReadOnly]
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]
    
