# Generated by Django 3.0.8 on 2021-08-11 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(default='Hola', max_length=100, unique=True, verbose_name='Nombre de Usuario')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo Electrónico')),
                ('nombre', models.CharField(blank=True, max_length=200, verbose_name='Nombre(s)')),
                ('apellido', models.CharField(blank=True, max_length=200, null=True, verbose_name='Apellido(s)')),
                ('imagen_perfil', models.ImageField(blank=True, default='perfil/sin_foto.png', max_length=200, null=True, upload_to='perfil/', verbose_name='Imagen de Perfil')),
                ('activo', models.BooleanField(default=True)),
                ('administrador', models.BooleanField(default=False)),
                ('slug', models.SlugField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
