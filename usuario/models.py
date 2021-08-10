from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,username,nombre,apellido,password=None):
        if not email:
            raise ValueError("El usuario debe tener un correo electronico")

        usuario = self.model(
            username = username, 
            email = self.normalize_email(email), 
            nombre = nombre, 
            apellido = apellido
            ) 
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self,email,username,nombre,apellido,password):
        #no se normaliza el email ni se encripta la password por que el 
        #metodo create_user ya lo hace
        usuario = self.create_user(
            email,
            username = username, 
            nombre = nombre, 
            apellido = apellido,
            password=password
        )
        usuario.administrador = True
        usuario.save()
        return usuario


class User(AbstractBaseUser):
    username = models.CharField('Nombre de Usuario',unique=True,max_length=100,default="Hola")
    email = models.EmailField("Correo Electrónico",unique=True,max_length=254)
    nombre = models.CharField("Nombre(s)", max_length=200,blank=True)
    apellido = models.CharField("Apellido(s)",max_length=200,blank=True,null=True)
    imagen_perfil = models.ImageField("Imagen de Perfil", upload_to="perfil/",  max_length=200,blank=True,null=True,default="sin_foto.png")
    activo = models.BooleanField(default=True)
    administrador = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','nombre','apellido']


    def __str__(self):
        return self.username

    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    

    @property
    def is_staff(self):
        return self.administrador
    

