from rest_framework import generics
from .models import Article, Category
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

# List and Create Articles
class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # Override get_queryset to filter by category slug if provided
    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.request.query_params.get('category_slug', None)
        
        # If category_slug is provided, filter articles by category
        if category_slug:
            try:
                category = Category.objects.get(slug=category_slug)
                queryset = queryset.filter(category=category)
            except Category.DoesNotExist:
                raise NotFound(detail="Category not found.")
        
        return queryset
    

class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'  # Use slug instead of pk

    def get(self, request, *args, **kwargs):
        # Get the article instance
        article = self.get_object()
        # Get related articles from the same category
        related_articles = Article.objects.filter(category=article.category).exclude(id=article.id)[:5]  # Limit to 5 articles

        # Serialize the related articles
        related_articles_data = ArticleSerializer(related_articles, many=True).data

        # Serialize the main article
        article_data = ArticleSerializer(article).data
        # Add related articles to the main article data
        article_data['related_articles'] = related_articles_data

        return Response(article_data)



