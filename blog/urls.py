from django.urls import path
from .views import PostList, PostDetail, list_category


urlpatterns = [
    path("", PostList.as_view(), name="homepage"),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('category/<str:tag>', list_category, name='category_list'),
]
