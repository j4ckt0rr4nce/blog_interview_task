from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, CategoryTag
from .views import PostList, PostDetail, CategoryList


class PostTests(APITestCase):
    fixtures = ['tag_fixtures.json', 'posts_fixtures.json']

    def setUp(self):
        self.test_post = Post.objects.get(title='Bunny')
        self.tag = CategoryTag.objects.get(name='pc')

    def tearDown(self):
        pass

    def test_view_posts(self):
        url = reverse('blog_api:list_post')
        response = self.client.get(url, format='json')
        self.assertEqual(resolve(url).func.view_class, PostList)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Squirrel')

    def test_post_detail(self):
        url = reverse('blog_api:detail_post', kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(resolve(url).func.view_class, PostDetail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Bunny')

    def test_view_category_list(self):
        self.test_post.tags.add(self.tag)
        url = reverse('blog_api:category_list', kwargs={'tag': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(resolve(url).func.view_class, CategoryList)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
