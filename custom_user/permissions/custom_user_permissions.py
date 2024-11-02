from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """custom permission to only allow owners of an object to edit it -> to be reworked"""
    ...
