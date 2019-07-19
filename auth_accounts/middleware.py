from rest_framework.permissions import BasePermission
from .models import CustomerSession


class CustomerPermission(BasePermission):
    def has_permission(self, request, view):
        if "HTTP_AUTHORIZATION" not in request.META:
            return False

        session = CustomerSession.objects.filter(
            token=request.META["HTTP_AUTHORIZATION"]
        ).first()
        if not session:
            return False

        request.customer_id = session.customer_id
        request.token = session.token
        return True
