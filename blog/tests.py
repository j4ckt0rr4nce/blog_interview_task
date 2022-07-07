from django.test import TestCase
from .models import Post, CategoryTag
from django.urls import reverse


class PostTesting(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='Panda', content='Panda is bear-like animal and climb trees.',
                                        image='panda.png')
        self.tag1 = CategoryTag.objects.create(name='animal')
        self.tag2 = CategoryTag.objects.create(name='food')

    def test_post_model(self):
        self.post.tags.add(self.tag1)
        self.post.tags.add(self.tag2)
        self.assertTrue(isinstance(self.post, Post))
        self.assertEqual(str(self.post), 'id: 1, title: Panda')
        self.assertEqual(str(self.tag1), 'id: 1, name: animal')
        self.assertEqual(str(self.tag2), 'id: 2, name: food')
        self.assertEqual(str(Post._meta.verbose_name_plural), "Posts")

    def test_list_view(self):
        url = reverse('homepage')
        response = self.client.get(url)
        self.assertTrue(response, url)
        self.assertTemplateUsed('homepage.html')
        self.assertContains(response, 'Panda')
        self.assertContains(response, 'Panda is bear-like animal and climb trees.')

    def test_list_detail(self):
        url = reverse('post_detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertTrue(response, url)
        self.assertTemplateUsed('post_detail.html')
        self.assertContains(response, 'Panda')
        self.assertContains(response, 'Panda is bear-like animal and climb trees.')

    def test_view_category_list(self):
        self.post.tags.add(self.tag1)
        url = reverse('category_list', kwargs={'tag': 1})
        response = self.client.get(url)
        self.assertTrue(response, url)
        self.assertTemplateUsed('tag.html')
