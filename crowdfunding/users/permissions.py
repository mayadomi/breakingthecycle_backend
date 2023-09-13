from rest_framework import permissions

class IsUserOrReadOnly(permissions.BasePermission):    

    def has_object_permission(self, request, view, obj):
        
        if (request.method in permissions.SAFE_METHODS) or request.method == 'PUT':
            if obj == request.user:
                return True   

