from rest_framework import serializers
from .models import Comments
from users.serializers import UserSerializer


class CommentsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = ["id", "comment", "created_at", "updated_at", "user"]
        read_only_fields = ["id", "created_at", "updated_at", "user"]
        depth = 1

    def create(self, validated_data: dict) -> Comments:
        comment = Comments.objects.create(**validated_data)

        return comment

    def update(self, instance: Comments, validated_data: dict) -> Comments:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
