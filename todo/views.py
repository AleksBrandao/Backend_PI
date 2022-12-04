from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer, GuardianSerializer, RolesSerializer, StudentsSerializer, AddressSerializer
from .models import Todo, Guardian, Roles, Students, Address

# Create your views here.
#teste novamente

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class GuardianView(viewsets.ModelViewSet):
    serializer_class = GuardianSerializer
    queryset = Guardian.objects.all()

class RolesView(viewsets.ModelViewSet):
    serializer_class = RolesSerializer
    queryset = Roles.objects.all()

class AddressView(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

class StudentsView(viewsets.ModelViewSet):
    serializer_class = StudentsSerializer
    queryset = Students.objects.all()
