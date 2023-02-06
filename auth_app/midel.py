from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission

class WhoAmI(BasePermission):
    def has_permission_doctor(self, request, view):
        if request.doctor == User:
            return True
        else:
            return False
    def has_permission_admin(self, request, view):
        if request.admin == User :
            return True
        else:
            return False
    def has_permission_studnt(self, request, view):
        if request.student == User :
            return True
        else:
            return False