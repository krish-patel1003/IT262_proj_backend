from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to eddit their own profile"""

    def has_permission(self, request, view):

        if request.method == "POST":
            self.message = "Student Profile is Already Created on Registration, User can only Update it"
            return False
        
        return True

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            """Allows users to view data but not edit"""
            return True
        
        return obj.user == request.user