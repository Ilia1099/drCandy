from rest_framework import permissions

SAFE_METHODS_FOR_USER_DATA = ("HEAD", "OPTIONS")


class IsAdminOrOwner(permissions.BasePermission):
    """custom permission to allow only owners of an object or admins to edit it """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS_FOR_USER_DATA:
            return True
        if not request.user.is_authenticated:
            return False
        is_admin_or_owner = request.user.is_superuser or obj.id == request.user.id
        return is_admin_or_owner


class IsOwner(permissions.BasePermission):
    """permission which checks if the user is an owner of the object"""
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        return obj.id == request.user.id
