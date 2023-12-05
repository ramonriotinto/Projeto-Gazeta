from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Posts
from .permission import IsAdminOrPostOwner
from .serializers import PostsSerializer
from users.permission import IsAdminOrAccountOwner


class PostsView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrAccountOwner]

    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListAllPostsView(ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class ListPostsUserView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrAccountOwner]

    serializer_class = PostsSerializer

    def get_queryset(self):
        user_id = self.request.user

        if self.request.user.is_superuser:
            return Posts.objects.all()

        return Posts.objects.filter(user=user_id)


class RetrieveUpdateDeletePost(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrPostOwner]

    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

    lookup_url_kwarg = "post_id"
