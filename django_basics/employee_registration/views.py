from employee_registration.models import Company
from employee_registration.serializers import SignupSerializer, CompanySerializer, EmployeeSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        response_data = SignupSerializer(user).data

        return Response(data=response_data, status=status.HTTP_201_CREATED)


class CompaniesListView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class EmployeeView(APIView):
    def put(self, request):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
