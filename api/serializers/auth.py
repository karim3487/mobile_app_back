from django.apps import apps
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.generics import get_object_or_404
from rest_framework.validators import UniqueValidator

from api.models.user import User


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=164, required=True)
    last_name = serializers.CharField(max_length=164, required=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        # validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True
    )

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"]
        )

        user.set_password(validated_data["password"])
        user.save()
        return user

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn\"t match."})

        return attrs


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
    )
    password = serializers.CharField(
        required=True
    )


class TokenSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "surname", "email", "profession",
                  "token"]

    def get_token(self, obj):
        return Token.objects.get_or_create(user=obj)[0].key