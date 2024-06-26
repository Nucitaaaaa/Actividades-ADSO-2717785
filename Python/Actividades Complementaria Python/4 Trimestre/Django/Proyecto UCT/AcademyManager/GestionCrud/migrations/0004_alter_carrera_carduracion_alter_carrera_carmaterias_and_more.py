# Generated by Django 4.2.6 on 2024-04-03 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionCrud', '0003_alter_estudiante_estfoto_alter_profesor_proffoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrera',
            name='carDuracion',
            field=models.CharField(max_length=50, verbose_name='Duración'),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='carMaterias',
            field=models.CharField(max_length=50, verbose_name='Materias'),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='carNombre',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='estApellido',
            field=models.CharField(max_length=50, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='estCarrera',
            field=models.CharField(max_length=50, verbose_name='Carrera'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='estEmail',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='estFechaActualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='estFechaCreacion',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='estFechaNacimiento',
            field=models.DateField(verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='estFoto',
            field=models.ImageField(default='null', upload_to='estFotos', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='estNombre',
            field=models.CharField(max_length=30, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='estTelefono',
            field=models.IntegerField(max_length=10, verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='materia',
            name='matCarrera',
            field=models.CharField(max_length=50, verbose_name='Carrera'),
        ),
        migrations.AlterField(
            model_name='materia',
            name='matCreditos',
            field=models.IntegerField(max_length=5, verbose_name='Creditos'),
        ),
        migrations.AlterField(
            model_name='materia',
            name='matDescripcion',
            field=models.TextField(verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='materia',
            name='matFechaActualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='materia',
            name='matFechaCreacion',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='materia',
            name='matNombre',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='materia',
            name='matProfesores',
            field=models.CharField(max_length=30, verbose_name='Profesores'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='profApellido',
            field=models.CharField(max_length=50, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='profCMaterias',
            field=models.CharField(max_length=50, verbose_name='Materias'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='profEmail',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='profFechaActualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='profFechaCreacion',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='profFechaNacimiento',
            field=models.DateField(verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='profFoto',
            field=models.ImageField(default='null', upload_to='profFotos', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='profNombre',
            field=models.CharField(max_length=30, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='profTelefono',
            field=models.IntegerField(max_length=10, verbose_name='Telefono'),
        ),
    ]
