from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsDoctor(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_doctor

class SymptomPermission(BasePermission):
    message = "Only Doctor can post/patch new symptom with verified tag."

    def has_permission(self, request, view):

        if request.method == "POST":
            # print("checking post request", (request.data.keys()))
            if "is_verified" in list(request.data.keys()):
                
                return request.user.is_doctor
        return True

    def has_object_permission(self, request, view, obj):
 
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_doctor or request.user.is_superuser

class AppointmentPremission(BasePermission):

    def has_permission(self, request, view):
        # print("method", request.method)
        if request.method == "POST":
            # print("checking post request", (request.data.keys()))
            if "prescription_id" in list(request.data.keys()):
                self.message = "prescription_id is auto added to appointment."
                return False
            if "student" in list(request.data.keys()):
                self.message = "the appoinment is created for logged in student only."
                return False
            if "status" in list(request.data.keys()):
                self.message = "Status By default is Pending, Only Doctor can update it"
                return False
            
            self.message = "Only Students can book Appointments"
            return not request.user.is_doctor
        
        if request.method == 'PATCH':
            # print("PUT and PATCH request")
            self.message = "Only Doctors or Admin can update appointment"
            return request.user.is_doctor or request.user.is_superuser
        
        return True

    def has_object_permission(self, request, view, obj):
        # print("method", request.method)

        if request.method in SAFE_METHODS:
            return True
        
        if request.method == 'DELETE':
            self.message = "The student who created appointment can only delete it."
            return (obj.student.user == request.user) or request.user.is_superuser


class PrescriptionPermission(BasePermission):
        
    def has_permission(self, request, view):
        if request.method == "POST":
            self.message = "prescription_id is auto added to appointment."
            return False
        if request.method == 'PATCH':
            self.message = "Only Doctors or Admin can update an appointment"
            return request.user.is_doctor or request.user.is_superuser
        return True

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        if request.method == "DELETE":
            self.message = "The student who created appointment can only delete it."
            return (obj.student.user == request.user) or request.user.is_superuser
    
        return request.user.is_doctor or request.user.is_superuser