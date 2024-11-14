from rest_framework import permissions


class IsWriterOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow:
    - Writer users to add, edit, and view.
    - Public (unauthenticated) users to only view.
    """

    def has_permission(self, request, view):


        if request.method in permissions.SAFE_METHODS:
            return True


        if request.user and request.user.is_authenticated:
            if request.user.groups.filter(name='writer').exists():
                return request.method in ['GET', 'POST', 'PUT', 'PATCH']

        return False
