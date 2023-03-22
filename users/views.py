from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.conf import settings
from django.middleware import csrf
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer, LogoutSerializer
from .utils import get_tokens_for_user
from rest_framework import permissions
from .models import StudentProfile


class HomeView(GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        return Response({"msg":"Yes I see u r authenticated", "user":request.user.email})


class RegisterView(GenericAPIView):

    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        data = request.data
        serializer = self.serializer_class(data=data)

        if "is_doctor" in request.data.keys():
            serializer.initial_data["is_doctor"] = True
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {"data": serializer.data, "mssg": "Doctor created"}, status=status.HTTP_201_CREATED)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        student = StudentProfile.objects.create(user=serializer.instance)

        return Response(
            {"data": serializer.data, "mssg": "user created"}, status=status.HTTP_201_CREATED)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        data = request.data
        response = Response()
        email = data.get('email', None)
        password = data.get('password', None)
        print("email = ", email, "password = ", password)
        user = authenticate(email=email, password=password)

        if user is not None:
            if user.is_active:
                data = get_tokens_for_user(user)
                response.set_cookie(
                    key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                    value=data['access'],
                    expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )
                response.set_cookie(
                    'refresh_token', data['refresh'], httponly=True)
                csrf.get_token(request)
                response.data = {
                    "Success": " Login Successfully!!", "data": data}
                return response
            else:
                return Response({"No active": "This account is not active"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Invalid": " Invalid email or password"}, status=status.HTTP_404_NOT_FOUND)


class LogoutView(GenericAPIView):

    serializer_class = LogoutSerializer

    def post(self, request, format=None):
        refresh_token = request.data['refresh_token']
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"msg": "Logout successful"})
