from django.db.models import Count, Sum
from rest_framework import serializers

from api.models import Ad, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name",  "surname", "profession"]