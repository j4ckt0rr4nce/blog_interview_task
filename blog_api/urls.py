from .views import PostList, PostDetail, CategoryList
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


app_name = 'blog_api'

urlpatterns = [
    path('post/', PostList.as_view(), name='list_post'),
    path('post/<str:pk>/', PostDetail.as_view(), name='detail_post'),
    path('post/category/<str:tag>', CategoryList.as_view(), name='category_list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
