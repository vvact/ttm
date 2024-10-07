from django.test import TestCase

from django.test import TestCase

# tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Article, Category
from django.contrib.auth.models import User

class ArticleAPITests(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Test Category", slug="test-category")
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.article_data = {
            'title': 'Test Article',
            'slug': 'test-article',
            'content': 'This is a test article.',
            'category': self.category.id,
            'author': self.user.id,
            'status': 'draft'
        }

    def test_create_article(self):
        response = self.client.post(reverse('article-list'), self.article_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Article.objects.count(), 1)

    def test_get_articles(self):
        Article.objects.create(**self.article_data)
        response = self.client.get(reverse('article-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_article(self):
        article = Article.objects.create(**self.article_data)
        updated_data = {'title': 'Updated Test Article'}
        response = self.client.put(reverse('article-detail', args=[article.id]), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        article.refresh_from_db()
        self.assertEqual(article.title, 'Updated Test Article')

    def test_delete_article(self):
        article = Article.objects.create(**self.article_data)
        response = self.client.delete(reverse('article-detail', args=[article.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Article.objects.count(), 0)





