from rest_framework import serializers
from .models import Todo, Roles, Guardian, Address, Students

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')

class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = ('id','nome', 'email', 'cpf', 'rg', 'telefone', 'Data_de_nascimento')

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ('id','função')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id','rua', 'número', 'complemento', 'bairro', 'cidade', 'estado', 'cep')

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('id', 'nome', 'email', 'cpf', 'rg', 'telefone', 'data_de_nascimento',)
        # fields = ('id','name', 'email')