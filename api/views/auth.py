from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from api.serializers.auth import (
    RegisterSerializer, TokenSerializer, LoginSerializer
)
from api.serializers.user import UserSerializer


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == "register_user":
            return RegisterSerializer
        if self.action == "login":
            return LoginSerializer

    def register(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        print(request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            login_serializer = LoginSerializer(request.data)
            return self.get_token(login_serializer)

        return Response({"message": "Can not create user."},
                        status=status.HTTP_400_BAD_REQUEST)

    def get_token(self, serializer, status_code=status.HTTP_201_CREATED):
        user = get_object_or_404(get_user_model(),
                                 email=serializer.data['email'])

        if user.check_password(serializer.data['password']):
            ser = TokenSerializer(user, many=False)

            return Response(
                ser.data,
                status=status_code
            )
        else:
            return Response({
                "detail": "Password is incorrect."
            }, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=RegisterSerializer,
                         responses={201: TokenSerializer(many=False)})
    @action(detail=False, methods=["POST"])
    def register_user(self, request, *args, **kwargs):
        """
        Register new user.
        """
        return self.register(request, *args, **kwargs)

    @swagger_auto_schema(request_body=LoginSerializer,
                         responses={200: TokenSerializer(many=False)})
    @action(detail=False, methods=["POST"])
    def login(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return self.get_token(serializer, status_code=status.HTTP_200_OK)
