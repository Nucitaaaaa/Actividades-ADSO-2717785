# Generated by Django 4.2.6 on 2024-04-04 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestionCrud', '0008_alter_carrera_carmaterias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrera',
            name='carMaterias',
            field=models.ManyToManyField(blank=True, to='GestionCrud.materia', verbose_name='Materias'),
        ),
        migrations.AlterField(
            model_name='materia',
            name='matProfesores',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GestionCrud.profesor', verbose_name='Profesor'),
        ),
    ]
