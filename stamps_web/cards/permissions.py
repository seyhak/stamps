from rest_framework import permissions
from django.core.exceptions import ObjectDoesNotExist


class IsCompanysUserCardType(permissions.BasePermission):
    """
    Allow only companys users to see card types.
    """
    def has_object_permission(self, request, view, obj):
        company_user = getattr(request.user, 'companyuser')
        is_user_in_company = obj.company == company_user.company
        return is_user_in_company


class IsAllowedToIncrementStamps(permissions.BasePermission):
    """
    Allow only companys users to see increment card stamps.
    """
    def has_object_permission(self, request, view, obj):
        try:
            company_user = getattr(request.user, 'companyuser')
            is_user_in_company = obj.card_type.company == company_user.company
            return is_user_in_company
        except ObjectDoesNotExist:
            return False


class IsCardOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.card_owner == request.user
