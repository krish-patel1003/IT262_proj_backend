from rest_framework.permissions import BasePermission, SAFE_METHODS

class SymptomPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == "POST":
            print("checking post request", (request.data.keys()))
            if "is_verified" in list(request.data.keys()):
                return request.user.is_doctor
        return True

    def has_object_permission(self, request, view, obj):
        print(request.method)

        if request.method in SAFE_METHODS:
            return True

        return request.user.is_doctor