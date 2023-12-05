from django.urls import path
from .views import CommentsView, RetrieveUpdateDeleteCommentView

urlpatterns = [
    path("comments/<uuid:post_id>/", CommentsView.as_view()),
    path("comment/<uuid:comment_id>/", RetrieveUpdateDeleteCommentView.as_view()),
]
