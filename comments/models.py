import uuid
from django.db import models


class Comments(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    comment = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="comments"
    )

    post = models.ForeignKey(
        "posts.Posts", on_delete=models.CASCADE, related_name="comments"
    )
