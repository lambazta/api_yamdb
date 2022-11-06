from rest_framework import permissions


class IsAdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.role == 'admin' or request.user.is_superuser
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.user.role == 'admin' or request.user.is_superuser
        )


class IsModeratorPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.role == 'moderator'
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.user.role == 'moderator'
        )
from rest_framework import permissions


class AuthorizedOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            obj.author == request.user
            or request.user.role == 'Admin'
            or request.user.role == 'Moderator'
        )
