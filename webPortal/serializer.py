from .models import WebPortal
from rest_framework import serializers


class WebPortalSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebPortal
        fields = "__all__"
