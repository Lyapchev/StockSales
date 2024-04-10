from rest_framework import serializers
from .models import Stock, Comment, Post

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('id', 'title', 'description', 'price', 'created_at', 'updated_at')
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
        
class CommentOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['title']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentOnlySerializer(many=True, read_only=True)
    #author = 
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author', 'created_at', 'updated_at', 'comments')