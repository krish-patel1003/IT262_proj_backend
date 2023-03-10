from rest_framework.permissions import BasePermission, SAFE_METHODS

class NoticePermission(BasePermission):
    message = "Only Doctor or Admin can Post/Patch/Delete a Notice."

    def has_permission(self, request, view):

        if request.method == "POST":
            return request.user.is_doctor or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
 
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_doctor or request.user.is_superuser