from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.user.is_authenticated, request.user)
        return request.user.is_authenticated and obj.user == request.user
