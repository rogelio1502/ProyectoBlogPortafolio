from django import forms
from django.contrib.auth.forms import UserCreationForm
from usuario.models import User

class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','username', 'password1' ,'password2','imagen_perfil' )
    
    


