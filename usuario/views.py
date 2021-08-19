from django.shortcuts import render,redirect

# Create your views here.
from usuario.forms import UserCreation
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView,PasswordChangeForm,PasswordChangeView,PasswordChangeDoneView
from django.views.generic import ListView, DetailView
from .models import User,UserManager
from posts.views import SearchForm


class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'accounts/change_done.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            
            'search_form': SearchForm()
        })
        #print(context)
        return context





class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'accounts/change.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            
            'search_form': SearchForm()
        })
        #print(context)
        return context
    


class SignUpView(generic.CreateView):
    form_class = UserCreation
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            
            'search_form': SearchForm()
        })
        #print(context)
        return context
    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            #super().get(request, *args, **kwargs)
            return redirect('list')
        return super().get(request, *args, **kwargs)
    

            
    

class LoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            
            'search_form': SearchForm()
        })
        #print(context)
        return context
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            #super().get(request, *args, **kwargs)
            return redirect('list')
        else:
            #print("Hola")
            return super().get(request, *args, **kwargs)



class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            
            'search_form': SearchForm()
        })
        #print(context)
        return context
    """
    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(
            *args, object_list=self.get_queryset(), **kwargs)
        context.update({
            "Saludo": "Hola mundo"
        })
        return context

    def get_queryset(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        # forma 1 y personalizable
        #print(self.get_context_data())
        if request.is_ajax():
            
            #lista_usuarios = []
            #for usuario in self.get_queryset():
             #   data_usuario = {}
              #  data_usuario["id"]=usuario.id
               # data_usuario["username"]=usuario.username
                #lista_usuarios.append(data_usuario)

            #print(lista_usuarios)
            #data = json.dumps(lista_usuarios)
            #forma 2 no personalizable
            
            data = serialize('json', self.get_queryset())
            return HttpResponse(data, 'application/json')
        #print(self.get_context_data())
        return render(request, self.template_name, self.get_context_data())
    """


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            
            'search_form': SearchForm()
        })
        #print(context)
        return context
   