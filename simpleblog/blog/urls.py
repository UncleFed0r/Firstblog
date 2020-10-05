from django.urls import path
from .views import PostsList, PostDetail, TagDetail, TagList, AuthorList
from .views import PostCreate, PostUpdate, PostDelete, TagCreate
from .views import UserLoginView, UserLogoutView, AuthorPosts

urlpatterns = [
    path('', PostsList.as_view(), name='posts_list_url'),
    path('login/', UserLoginView.as_view(), name='user_login_url'),
    path('logout/', UserLogoutView.as_view(), name='user_logout_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<slug:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<slug:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('post/<slug:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<slug:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tags/', TagList.as_view(), name='tags_list_url'),
    path('authors/', AuthorList.as_view(), name='authors_list_url'),
    path('author/<slug:name>/', AuthorPosts.as_view(), name='author_posts_url'),
]
