from .serializer import WebPortalSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .pagination import StandardResultsSetPagination
from .models import WebPortal


class WebPortalViewSet(viewsets.ModelViewSet):

    queryset = WebPortal.objects.all()
    serializer_class = WebPortalSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]
    throttle_scope = "user-web-portal"
