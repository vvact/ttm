from django.urls import path
from .views import ArticleListCreateView

urlpatterns = [
    path('articles/', ArticleListCreateView.as_view(), name='article-list-create'),
    path('articles/<slug:slug>/', ArticleListCreateView.as_view(), name='article-detail'),
]
