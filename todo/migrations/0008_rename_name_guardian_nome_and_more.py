# Generated by Django 4.0.5 on 2022-06-29 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_rename_city_address_bairro_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guardian',
            old_name='name',
            new_name='nome',
        ),
        migrations.RemoveField(
            model_name='guardian',
            name='dateOfBirth',
        ),
        migrations.RemoveField(
            model_name='guardian',
            name='phone',
        ),
        migrations.AddField(
            model_name='guardian',
            name='Data_de_nascimento',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='guardian',
            name='telefone',
            field=models.IntegerField(blank=True, default=111111111),
        ),
        migrations.AlterField(
            model_name='address',
            name='rua',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='guardian',
            name='cpf',
            field=models.IntegerField(blank=True, default=11111111111),
        ),
        migrations.AlterField(
            model_name='guardian',
            name='email',
            field=models.EmailField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='guardian',
            name='rg',
            field=models.IntegerField(blank=True, default=111111111),
        ),
    ]
