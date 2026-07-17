from rest_framework.permissions import BasePermission



class IsLibarianOrAdmin(BasePermission):
    """
    Custom permission to allow access only to users with the 'libarian' or 'admin' role.
    """
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (
            user.role == "libarian" or user.is_staff or user.is_superuser
    )