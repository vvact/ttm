from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, CategoryViewSet

from .views import ArticlesByCategoryView

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/articles/<slug:slug>/', ArticleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='article-detail'),
    path('api/categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category-detail'),
    path('api/categories/<int:id>/articles/', ArticlesByCategoryView.as_view(), name='articles-by-category'),
    path('api/articles/search/', ArticleViewSet.as_view({'get': 'list'}), name='article-search'),  # This can be for searching

]
