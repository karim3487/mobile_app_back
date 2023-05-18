from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.models import Attachment
from api.permissions.permissions import AttachmentAccessPolicy
from api.serializers.attachment import AttachmentSerializer


class AttachmentViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    permission_classes = (AttachmentAccessPolicy, )

    def get_queryset(self):
        return AttachmentAccessPolicy.scope_queryset(self.request, Attachment.objects.all(), self.action)

    def get_serializer_class(self):
        return AttachmentSerializer