from rest_framework import permissions


class IsDonorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        print(obj.donor)
        print(request.user)
        return obj.donor == request.user

class IsRiderOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        print(obj.rider)
        print(request.user)
        return obj.rider == request.user