from django.test import TestCase
from .models import Post, CategoryTag
from django.urls import reverse, resolve
from .views import PostList, PostDetail, list_category


class PostTesting(TestCase):
    fixtures = ['tag_fixtures.json', 'posts_fixtures.json']

    def setUp(self):
        self.post = Post.objects.get(title='Bunny')
        self.tag1 = CategoryTag.objects.get(name='pc')
        self.tag2 = CategoryTag.objects.get(name='smartphone')

    def tearDown(self):
        pass

    def test_post_model(self):
        self.post.tags.add(self.tag1)
        self.post.tags.add(self.tag2)
        self.assertTrue(isinstance(self.post, Post))
        self.assertEqual(str(self.post), 'id: 1, title: Bunny')
        self.assertEqual(str(self.tag1), 'id: 1, name: pc')
        self.assertEqual(str(self.tag2), 'id: 7, name: smartphone')
        self.assertEqual(str(Post._meta.verbose_name_plural), "Posts")

    def test_list_view(self):
        url = reverse('homepage')
        response = self.client.get(url)
        self.assertTrue(response, url)
        self.assertTemplateUsed('homepage.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resolve(url).func.view_class, PostList)

    def test_list_detail(self):
        url = reverse('post_detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertTrue(response, url)
        self.assertTemplateUsed('post_detail.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resolve(url).func.view_class, PostDetail)
        self.assertContains(response, 'Bunny')
        self.assertContains(response, 'Rabbits, also known as bunnies or bunny rabbits, are small mammals')

    def test_view_category_list(self):
        self.post.tags.add(self.tag1)
        url = reverse('category_list', kwargs={'tag': 1})
        response = self.client.get(url)
        self.assertTrue(response, url)
        self.assertTemplateUsed('tag.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resolve(url).func, list_category)
