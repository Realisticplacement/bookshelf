from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthenticateduser(BasePermission):
    """
    Custom permission to allow access only to authenticated users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    

class IsLibarianOrAdmin(BasePermission):
    """
    Custom permission to allow access only to users with the 'libarian' or 'admin' role.
    """
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (
            user.role == "librarian" or user.is_staff or user.is_superuser
    )