from rest_framework import permissions
from django.contrib.auth.models import User
from accounts.models import User
from accounts.permissions import IsAuthenticateduser, IsLibarianOrAdmin



class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
    

class IsOwner(permissions.BasePermission):
   def has_object_permission(self, request, view, obj):
        return obj.user == request.user
