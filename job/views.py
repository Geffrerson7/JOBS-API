from .pagination import StandardResultsSetPagination
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from .serializer import JobSerializer
from .models import Job


class JobViewSet(viewsets.ModelViewSet):

    queryset = Job.objects.all().order_by("id")
    serializer_class = JobSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ["company", "publicationDate", "portal_name"]
    throttle_scope = "job"
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user.id)