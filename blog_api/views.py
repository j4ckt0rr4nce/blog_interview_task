from django.shortcuts import get_object_or_404
from blog.models import Post
from .serializers import PostSerializer
from rest_framework import generics


class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetail(generics.RetrieveAPIView):
    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, pk=item)


class CategoryList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        tag = self.kwargs.get('tag')
        return Post.objects.filter(tags__name=tag).order_by('-id')
