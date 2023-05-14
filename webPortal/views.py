from .serializer import WebPortalSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .pagination import StandardResultsSetPagination
from .models import WebPortal


class WebPortalViewSet(viewsets.ModelViewSet):

    queryset = WebPortal.objects.all().order_by("id")
    serializer_class = WebPortalSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]
    throttle_scope = "web-portal"
    
