from rest_framework import serializers


class ProfessorListSerializer(serializers.Serializer):
    t_id = serializers.IntegerField()
    name = serializers.CharField()
