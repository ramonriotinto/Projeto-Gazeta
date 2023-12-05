import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(
        max_length=20, unique=True, error_messages={"unique": "Username already in use"}
    )
    email = models.EmailField(max_length=127, unique=True)
    password = models.CharField(max_length=127)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    img_avatar = models.CharField(max_length=500, null=True)
