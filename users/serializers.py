from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="user with this email already exists.",
            )
        ],
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
            "is_active",
            "is_superuser",
            "created_at",
            "updated_at",
            "img_avatar",
        ]
        read_only_fields = ["id", "updated_at", "is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}
        depth = 1

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance
