from rest_framework import serializers

from api.models.group import Group


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = "__all__"
