from django.contrib import admin
from .models import Todo, Guardian, Roles, Students, Address, About, Cursos, Professores

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

class GuardianAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'rg', 'telefone', 'Data_de_nascimento')

class RolesAdmin(admin.ModelAdmin):
    list_display = ('função', )

class StudentsAdmin(admin.ModelAdmin):
    list_display =  ('nome', 'email', 'cpf', 'rg', 'telefone', 'data_de_nascimento', )

class AddressAdmin(admin.ModelAdmin):
    list_display = ('rua', 'número', 'complemento', 'bairro', 'cidade', 'estado', 'cep')

# Register your models here.
class CursosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'materiais', 'duracao', 'idade', 'Investimento', 'preço')

class AboutAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao1', 'descricao1')

class ProfessoresAdmin(admin.ModelAdmin):
    list_display = ('instagran', 'descricao', 'foto')



admin.site.register(Todo, TodoAdmin)
admin.site.register(Guardian, GuardianAdmin)
admin.site.register(Roles, RolesAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Students, StudentsAdmin)
admin.site.register(Cursos, CursosAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Professores, ProfessoresAdmin)

