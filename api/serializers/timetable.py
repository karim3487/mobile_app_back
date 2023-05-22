from rest_framework import serializers

from api.serializers.professors import ProfessorListSerializer


class SubjectListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    start = serializers.CharField()
    end = serializers.CharField()
    classroom = serializers.CharField()
    professors = serializers.ListField(child=ProfessorListSerializer())


class TimetableListSerializer(serializers.Serializer):
    is_even = serializers.BooleanField()
    code = serializers.CharField()
    day = serializers.IntegerField()
    all_subjects = serializers.ListField(child=SubjectListSerializer())
