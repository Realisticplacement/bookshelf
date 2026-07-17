from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsBookManagerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user
        if not user or not user.is_authenticated:
            return False

        is_librarian = getattr(user, "role", None) == "libarian"
        is_admin = getattr(user, "is_superuser", False) or getattr(user, "is_staff", False)

        if request.method in {"POST", "DELETE"}:
            return is_librarian or is_admin

        return is_admin

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user
        if not user or not user.is_authenticated:
            return False

        is_admin = getattr(user, "is_superuser", False) or getattr(user, "is_staff", False)
        is_librarian = getattr(user, "role", None) == "libarian"

        if request.method == "DELETE":
            return is_admin or (
                is_librarian and getattr(obj, "uploaded_by", None) == user
            )

        return is_admin


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
