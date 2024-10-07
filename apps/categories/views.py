from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer

# List and Create Categories
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



