from rest_framework import permissions

# Skapa ett custom permission för att låte en användare ändra på något om hen är ägaren
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
    #Admin har tillgång till allt
        if request.user.is_staff:
            return True
    #En användare ska bara kunna redigera sina egna inlägg

        return obj.user == request.user