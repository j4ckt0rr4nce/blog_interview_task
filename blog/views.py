from django.shortcuts import render
from django.views. generic import ListView, DetailView
from django.core.paginator import Paginator
from .models import Post


class PostList(ListView):
    queryset = Post.objects.all()
    template_name = "blog/homepage.html"
    paginate_by = 3


class PostDetail(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


def list_category(request, tag):
    posts = Post.objects.filter(tags__name=tag).order_by('-id')
    paginator = Paginator(posts, 3)
    page_num = request.GET.get('page', 1)
    posts = paginator.page(page_num)

    context = {
        'posts': posts,
        'tag': tag
              }

    return render(request, 'blog/tag.html', context)
