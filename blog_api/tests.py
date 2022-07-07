from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, CategoryTag
from .views import PostList, PostDetail, CategoryList


class PostTests(APITestCase):
    def setUp(self):
        self.test_post = Post.objects.create(title='Panda', content='Panda is bear-like animal and climb trees.',
                                             image='panda.png')
        self.tag = CategoryTag.objects.create(name='animal')

    def tearDown(self):
        pass

    def test_view_posts(self):
        url = reverse('blog_api:list_post')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(resolve(url).func.view_class, PostList)

    def test_post_detail(self):
        url = reverse('blog_api:detail_post', kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(resolve(url).func.view_class, PostDetail)

    def test_view_category_list(self):
        self.test_post.tags.add(self.tag)
        url = reverse('blog_api:category_list', kwargs={'tag': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(resolve(url).func.view_class, CategoryList)
