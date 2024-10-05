from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q  # Import Q for complex queries
from .models import Article, Category
from .serializers import ArticleSerializer, CategorySerializer
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q


class ArticlesByCategoryView(ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        # Retrieve the category based on the ID from the URL
        category_id = self.kwargs['id']  # Ensure 'id' matches your URL pattern
        # Filter articles that belong to this category and are published
        return Article.objects.filter(category__id=category_id, is_published=True)

    def get(self, request, *args, **kwargs):
        # Fetch and return articles for the given category
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ['published_at', 'title']
    ordering = ['-published_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Get search parameters from the request
        search_query = self.request.query_params.get('search', None)

        # Filter by search query in title or content
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(content__icontains=search_query)
            )

        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'
