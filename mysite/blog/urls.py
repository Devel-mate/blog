from django.urls import path
from .import views
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    # Post list
    path('', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    # Post list with tags as parameters
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    # Post detail page
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    # Post sharing page
    path('<int:post_id>/share/', views.post_share, name= 'post_share'),
    # Process comment function
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    # RSS
    path('feed/', LatestPostsFeed(), name='post_feed'),
    # Search page
    path('search/', views.post_search, name='post_search'),
]