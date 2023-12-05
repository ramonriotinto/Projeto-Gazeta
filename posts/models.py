import uuid
from django.db import models


class Posts(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=150)
    history = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    img_card = models.CharField(max_length=300)
    img_post_1 = models.CharField(max_length=300)
    img_post_2 = models.CharField(max_length=300)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="posts"
    )
