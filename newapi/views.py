from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pages.models import Products,Sku
from .models import Employees
from .serializers import EmployeesSerializer

class employeeList(APIView):
	"""docstring for empoyeeList"""
	def get(self, request):
		employee1=Employees.objects.all()
		serializer=EmployeesSerializer(employee1, many=True)
		return Response(serializer.data)
	