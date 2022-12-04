from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer, GuardianSerializer, RolesSerializer, StudentsSerializer, AddressSerializer
from .models import Todo, Guardian, Roles, Students, Address

from django.http import HttpResponse
from django.template import loader
from todo.models import Students

def index(request):
    students = Students.objects.order_by('id')
    guardian = Guardian.objects.order_by('id')
    

    template = loader.get_template('report.html')
    context = {
        'Students': students,
        'Guardians': guardian
    }
    return HttpResponse(template.render(context, request))

# Create your views here.

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
