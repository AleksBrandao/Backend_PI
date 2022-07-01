from django.contrib import admin
from .models import Todo, Guardian, Roles, Students, Address

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

admin.site.register(Todo, TodoAdmin)
admin.site.register(Guardian, GuardianAdmin)
admin.site.register(Roles, RolesAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Students, StudentsAdmin)

