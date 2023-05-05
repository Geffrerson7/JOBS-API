from .models import Job
from rest_framework import serializers
from webPortal.models import WebPortal


class JobSerializer(serializers.ModelSerializer):

    webPortal = serializers.SlugRelatedField(
        queryset=WebPortal.objects.all(), slug_field="name"
    )

    class Meta:
        model = Job
        fields = (
            "id",
            "name",
            "url",
            "company",
            "modality",
            "webPortal",
            "applicationDate",
            "publicationDate",
            "portal_logo",
            "user_email"
       )
        read_only_fields = "email", "applicationDate", "portal_logo"
