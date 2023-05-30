from django.contrib.auth.models import User
from rest_framework import serializers

from employee_registration.models import Company
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404


class SignupSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=8)
    username = serializers.CharField(min_length=8)
    password = serializers.CharField(write_only=True)

    def validate_username(self, data):
        if User.objects.filter(username=data).exists():
            raise ValidationError("The specified username is not available")

        return data

    def save(self, **kwargs):
        email = self.validated_data.get("email")
        username = self.validated_data.get("username")
        password = self.validated_data.get("password")

        user = User.objects.create(email=email, username=username, password=password)

        return user


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    foundation_date = serializers.CharField(read_only=True)
    domain = serializers.CharField(read_only=True)


class EmployeeSerializer(serializers.Serializer):
    user = serializers.CharField(write_only=True)
    company = serializers.IntegerField(write_only=True)

    def validate(self, attrs):
        user = attrs.get("user")
        company = attrs.get("company")

        company = get_object_or_404(Company, id=company)

        if company.employees.filter(username=user).exists():
            raise ValidationError("The specified user has already been registered")

        return attrs

    def save(self, **kwargs):
        user = self.validated_data.get("user")
        company = self.validated_data.get("company")

        user = get_object_or_404(User, username=user)
        company = get_object_or_404(Company, id=company)

        company.employees.add(user)
