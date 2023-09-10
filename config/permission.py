from rest_framework import permissions


class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.roles == 3


class AuthorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.roles == 3 or request.user.roles == 2


class AutherUserPermissions(permissions.BasePermission):
    
    # def has_permission(self, request, view):
    #     if not request.user.is_authenticated:
    #         return False
    #     return request.user.roles == 3 or request.user.roles == 2
    
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user and request.user.is_authenticated
