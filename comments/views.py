from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Comments
from posts.models import Posts
from .serializers import CommentsSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permission import IsAdminOrAccountOwner
from rest_framework.exceptions import APIException
from rest_framework import status
from django.shortcuts import get_object_or_404


class GetPost(APIException):
    status_code = status.HTTP_400_BAD_REQUEST


class CommentsView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrAccountOwner]

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    lookup_url_kwarg = "post_id"

    def perform_create(self, serializer):
        post_found = Posts.objects.filter(id=self.kwargs.get("post_id"))

        if not post_found:
            raise GetPost("The post does not exist")

        post = get_object_or_404(Posts, id=self.kwargs.get("post_id"))

        serializer.save(post=post, user=self.request.user)


class RetrieveUpdateDeleteCommentView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrAccountOwner]

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    lookup_url_kwarg = "comment_id"
