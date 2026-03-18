from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

# Skapa ett custom permission för att låte en användare ändra på något om hen är ägaren
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
    #Tillåt läsning för alla
        if request.method in SAFE_METHODS:
            return True
    #Admin har tillgång till allt
        if request.user.is_superuser:
            return True
    #En användare ska bara kunna redigera sina egna inlägg
        if hasattr(obj, 'user'):
            return obj.user == request.user
        return False