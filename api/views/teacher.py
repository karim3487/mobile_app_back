from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.models.teachers import Teacher
from api.serializers.teacher import TeacherSerializer


class TeacherViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):

    def get_queryset(self):
        return Teacher.objects.all()

    def get_serializer_class(self):
        return TeacherSerializer