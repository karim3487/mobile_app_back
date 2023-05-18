from django.db.models import Count, Sum
from rest_framework import serializers

from api.models import Ad
from api.serializers.user import UserSerializer


class AdListSerializer(serializers.ModelSerializer):
    creator = UserSerializer(many=False)

    class Meta:
        model = Ad
        fields = "__all__"