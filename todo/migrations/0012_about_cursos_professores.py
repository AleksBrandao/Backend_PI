# Generated by Django 4.0.5 on 2022-07-03 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_remove_students_endereço_remove_students_professor'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('descricao1', models.CharField(max_length=120)),
                ('descricao2', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('descricao', models.CharField(max_length=500)),
                ('materiais', models.CharField(max_length=120)),
                ('duracao', models.CharField(max_length=120)),
                ('idade', models.CharField(max_length=120)),
                ('Investimento', models.CharField(max_length=120)),
                ('preço', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Professores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagran', models.CharField(max_length=120)),
                ('descricao', models.CharField(max_length=120)),
                ('foto', models.CharField(max_length=120)),
            ],
        ),
    ]