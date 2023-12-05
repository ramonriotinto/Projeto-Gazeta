from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User


class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated and request.user.is_superuser
        else:
            return True


class IsAdminOrAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        return bool(request.user.id == obj.id or request.user.is_superuser)
