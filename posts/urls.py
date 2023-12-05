from django.urls import path
from .views import (
    PostsView,
    ListAllPostsView,
    ListPostsUserView,
    RetrieveUpdateDeletePost,
)

urlpatterns = [
    path("posts/", PostsView.as_view()),
    path("allposts/", ListAllPostsView.as_view()),
    path("listposts/", ListPostsUserView.as_view()),
    path("posts/<uuid:post_id>/", RetrieveUpdateDeletePost.as_view()),
]
