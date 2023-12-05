from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Posts


class IsAdminOrPostOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Posts):
        return bool(request.user.id == obj.user.id or request.user.is_superuser)
