from rest_framework import viewsets
from .models import Stock
from.serializers import StockSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class StockViewSet(viewsets.ModelViewSet):
    #queryset = Stock.objects.get_queryset().order_by('-id')
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]