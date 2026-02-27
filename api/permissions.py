from rest_framework import permissions

# Skapa ett custom permission för att låte en användare ändra på något om hen är ägaren
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user