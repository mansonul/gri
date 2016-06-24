from rest_framework import viewsets
from models import Ad, Category
from serializers import AdSerializer, CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Category objects """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AdViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Ad objects """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer