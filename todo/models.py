from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title

class Guardian(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField(max_length=120, blank = True)
    cpf = models.IntegerField(blank = True, default=11111111111)
    rg = models.IntegerField(blank = True, default=111111111)
    telefone = models.IntegerField(blank = True, default=111111111)
    Data_de_nascimento = models.CharField(max_length=10, blank = True)

    def _str_(self):
        return self.nome

class Meta:
        verbose_name = "Guardian"
        verbose_name_plural = "Guardians"

class Roles(models.Model):
    função = models.CharField(max_length=120)
   
    def _str_(self):
        return self.função

class Address(models.Model):
    rua = models.CharField(max_length=120)
    número = models.CharField(max_length=120, blank = True)
    complemento = models.CharField(max_length=120, blank = True)
    bairro = models.CharField(max_length=120, blank = True)
    cidade = models.CharField(max_length=120, blank = True)
    estado = models.CharField(max_length=120, blank = True)
    cep = models.CharField(max_length=120, blank = True)


    def _str_(self):
        return self.rua

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

class Students(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField(max_length=120, blank=True)
    cpf = models.IntegerField(blank=True, default=111111111)
    rg = models.IntegerField(blank=True, default=111111111)
    telefone = models.IntegerField(blank=True, default=111111111)
    data_de_nascimento = models.CharField(max_length=20, blank=True)
    # endereço = models.ForeignKey('Address', on_delete=models.CASCADE, null=True)
    # professor = models.ForeignKey('Guardian', on_delete=models.CASCADE, null=True)
    def _str_(self):
        return self.nome

