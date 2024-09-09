from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user
    

class HasListOrReadOnly(permissions.BasePermission):
    # message = 'У вас нет ни одного созданного списка'

    def has_permission(self, request, view):
        if view.action == 'create':
            return request.user.lists.exists()
        
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.list.user == request.user
    

class IsUserItselfOrDeny(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.username == request.user.username


# IsUserStaff - проверяет сотрудника
class IsStaffOrReadOnly(permissions.BasePermission):
    # ограниченный доступ к представлению
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.is_staff