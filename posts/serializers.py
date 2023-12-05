from rest_framework import serializers
from .models import Posts
from users.serializers import UserSerializer
from comments.serializers import CommentsSerializer


class PostsSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    user = UserSerializer(read_only=True)
    comments = CommentsSerializer(read_only=True, many=True)

    class Meta:
        model = Posts
        fields = [
            "id",
            "created_at",
            "updated_at",
            "img_card",
            "img_post_1",
            "img_post_2",
            "title",
            "description",
            "history",
            "user",
            "comments",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "user", "comments"]
        depth = 1

    def create(self, validated_data: dict) -> Posts:
        post = Posts.objects.create(**validated_data)

        return post

    def update(self, instance: Posts, validated_data: dict) -> Posts:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
