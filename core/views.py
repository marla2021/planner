from django.contrib.auth import login, logout
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
)
from rest_framework.response import Response

from core.models import User
from core.serializers import (
    CreateUserSerializer,
    LoginSerializer,
    UserSerializer,
    UpdatePasswordSerializer,
)


class SignupView(CreateAPIView):
    model = User
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        s: LoginSerializer = self.get_serializer(data=request.data)
        s.is_valid(raise_exception=True)
        username = s.validated_data["username"]
        user = User.objects.get(username=username)
        login(request, user=user)
        user_serializer = UserSerializer(instance=user)
        return Response(user_serializer.data)


class ProfileView(RetrieveUpdateDestroyAPIView):
    model = User
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({})


class UpdatePasswordView(UpdateAPIView):
    model = User
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdatePasswordSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        login(request=request, user=user, backend='django.contrib.auth.backends.Model')
        return JsonResponse(data=serializer.data, status=200)