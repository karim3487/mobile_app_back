from django.db.models import Count, Sum
from rest_framework import serializers

from api.models import Attachment


class AttachmentSerializer(serializers.ModelSerializer):
    size = serializers.SerializerMethodField()

    class Meta:
        model = Attachment
        fields = ["title", "file", "created_at", "size"]

    def get_size(self, obj):
        size = obj.file.size
        if size > 0:
            return round(size / 1024)
        return 0
