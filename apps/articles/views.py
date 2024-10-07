from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer

# List and Create Articles
class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

