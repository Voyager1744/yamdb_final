from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS, BasePermission


class OwnerOrAdmins(permissions.BasePermission):
    """Allowed for admin, superuser or owner"""

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (
                request.user.is_admin
                or request.user.is_superuser)
        )

    def has_object_permission(self, request, view, obj):
        print(request.user)
        return (
            obj == request.user
            or request.user.is_admin)


class IsAdminOrReadOnly(BasePermission):
    """Allowed to write only for admin"""

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or (
                request.user.is_authenticated
                and request.user.is_admin
            )
        )


class AuthorAndStaffOrReadOnly(BasePermission):
    """Allowed to write for admins and moderators"""

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or (
                request.user.is_authenticated
                and (
                    obj.author == request.user
                    or request.user.is_moderator
                )
            )
        )
