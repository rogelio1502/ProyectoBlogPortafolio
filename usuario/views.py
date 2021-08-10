from django.shortcuts import render,redirect

# Create your views here.
from usuario.forms import UserCreation
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView


class SignUpView(generic.CreateView):
    form_class = UserCreation
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            #super().get(request, *args, **kwargs)
            return redirect('list')
        return super().get(request, *args, **kwargs)

class LoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            #super().get(request, *args, **kwargs)
            return redirect('list')
        else:
            #print("Hola")
            return super().get(request, *args, **kwargs)

