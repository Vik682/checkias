from authentication.models import USER_ROLES
from rest_framework.permissions import BasePermission

#permissions match
class IsStudent(BasePermission):
    """
    Allows access only to students.
    """

    def has_permission(self, request, _):
        return bool(request.user and
        request.user.role == USER_ROLES['student'])
        
class IsCoaching(BasePermission):
    """
    Allows access only to Coachings.
    """

    def has_permission(self, request, _):
        return bool(request.user and
        request.user.role == USER_ROLES['coaching'])
        
class IsEvaluator(BasePermission):
    """
    Allows access only to only Evaluators.
    """

    def has_permission(self, request, _):
        return bool(request.user and
        request.user.role == USER_ROLES['evaluator'])

class IsReviewer(BasePermission):
    """
    Allows access only to only Reviewer.
    """

    def has_permission(self, request, _):
        return bool(request.user and
        request.user.role == USER_ROLES['reviewer'])
        
class IsEnquiry(BasePermission):
    """
    Allows access only to only Enquiry.
    """

    def has_permission(self, request, _):
        return bool(request.user and
        request.user.role == USER_ROLES['enquiry'])

class IsAdmin(BasePermission):
    """
    Allows access only to only Admins.
    """

    def has_permission(self, request, _):
        return bool(request.user and
        request.user.role == USER_ROLES['admin'])
        
class IsSuperuser(BasePermission):
    """
    Allows access only to only Superuser.
    """

    def has_permission(self, request, _):
        return bool(request.user and
        request.user.role == USER_ROLES['superuser'])