from rest_framework.permissions import BasePermission

class UserPermissions(BasePermission):

    def has_permission(self, request, view):
        if view.action == 'retrieve':
            return request.user.is_staff
        elif view.action == 'create':
            return True
        else:
            return request.user.is_authenticated
