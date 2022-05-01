from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password_repeat = serializers.CharField(write_only=True)

    class Meta:
        model = User
        read_only_fields = ("id",)
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "password_repeat",
        )

    def validate(self, datas):
        password = datas.get("password")
        password_repeat = datas.get("password_repeat")
        if password != password_repeat:
            raise ValidationError("Пароли не совпадают!")
        return datas

    def create(self, validated_data):
        validated_data['password'] = make_password(validate_password['password'])
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, datas):
        username = datas.get("username")
        password = datas.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError("Имя или пароль не верны!")
        datas["user"] = user
        return datas


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ("id",)
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
        )


class UpdatePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        read_only_fields = ("id",)
        fields = ("old_password", "new_password")


    def validate(self, datas: dict) -> dict:
        old_password = datas.get("old_password")
        user: User = self.instance
        if not user.check_password(old_password):
            raise ValidationError({'old_password': 'Поле заполненно не верно'})
        return datas

    def update(self, instance: User, validated_data):
        instance.set_password(validated_data["new_password"])
        instance.save(update_fields=["password"])
        return instance
