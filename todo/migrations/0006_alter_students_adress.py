# Generated by Django 4.0.5 on 2022-06-29 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_students_guardian'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='adress',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.address'),
        ),
    ]