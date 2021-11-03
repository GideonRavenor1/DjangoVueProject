from rest_framework import permissions
from .serializers import UsersSerializer


class CustomPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        data = UsersSerializer(request.user).data
        if data['role']:
            view_access = any(permission['name'] == f'view_{view.permission_object}' for permission in data['role']['permissions'])
            edit_access = any(permission['name'] == f'edit_{view.permission_object}' for permission in data['role']['permissions'])

            if request.method == 'GET':
                return view_access or edit_access

            return edit_access
        else:
            return False