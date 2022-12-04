from rest_framework import serializers
from .models import Todo, Roles, Guardian, Address, Students, About, Cursos, Professores

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

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id','titulo', 'descricao1', 'descricao1')

class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = ('id','titulo', 'descricao', 'materiais', 'duracao', 'idade', 'Investimento', 'preço')

class ProfessoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professores
        fields = ('instagran', 'descricao', 'foto')
        