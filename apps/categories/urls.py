from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryListCreateView


router = DefaultRouter()
router.register(r'categories', CategoryListCreateView)

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
]
