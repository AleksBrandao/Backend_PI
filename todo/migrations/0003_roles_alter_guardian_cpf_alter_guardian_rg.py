# Generated by Django 4.0.5 on 2022-06-26 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_guardian'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='guardian',
            name='cpf',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='guardian',
            name='rg',
            field=models.IntegerField(),
        ),
    ]
