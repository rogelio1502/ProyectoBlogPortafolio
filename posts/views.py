
import json
from bson import json_util
from datetime import datetime, timedelta

from django.http import HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.core.serializers import serialize
from .models import *
from .forms import PostForm, CommentForm,SearchForm

# Create your views here.








class PostListView(ListView):
    model = Post
    form = SearchForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # agregamos dos claves al contexto original
        context.update({
            'search_form': SearchForm()
            
        })
        return context

    def post(self, request, *args, **kwargs):
        print("En post")
        form = SearchForm(request.POST)
        if form.is_valid():
           
            criterio = (form.cleaned_data["search"])
            print(criterio)
            posts = Post.objects.filter(title__icontains=criterio)
            print(posts)
        return render(request,'posts/post_list.html',{'object_list':posts,'search_form':SearchForm})



    def get(self, request, *args, **kwargs):
        


        return super().get(request, *args, **kwargs)

    
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # agregamos dos claves al contexto original
        context.update({
            'form': CommentForm(),
            'object': self.object,
            'search_form': SearchForm()
        })
        return context

    def get(self, request, *args, **kwargs):
        post = self.get_object()

        if request.is_ajax():
            lista = list()
            comentarios = Comment.objects.filter(
                post=post).order_by('-id')
            # print("*"*50)
            for i in comentarios:
                # print(i.user)
                # print(i.content)
                # print(i.timestamp)
                comentarios_data = {}
                comentarios_data["id_comentario"] = i.id

                comentarios_data["user"] = i.user.username
                comentarios_data["content"] = i.content
                comentarios_data["time"] = i.timestamp
                
                _id = i.id
                try:
                    comment = Comment.objects.filter(id=_id)[0]
                    commentView = CommentView.objects.filter(comment=comment,user=request.user)[0]
                    #print("LLega aqui")
                    visto = True
                    
                
                except:
                    visto = False
                comentarios_data["visto"]=visto
                lista.append(comentarios_data)
            lista.append({"count": post.get_comment_count})

            # print(lista)
            # DjangoJSONEncoder es necesario para poder serializar fechas
            data = json.dumps(lista, cls=DjangoJSONEncoder)
            # print(data)
            # print(type(data))

            return HttpResponse(data, 'application/json')
        else:

            self.object = self.get_object()
            # print(self.object)
            # print(self.get_context_data())
            return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        print("**********"*20)
        # print(self.request.POST)
        # print("**********"*20)
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.instance
            comment.user = self.request.user
            comment.post = post
            comment.save()

        lista = []
        comentarios = Comment.objects.filter(post=post).order_by('-id')
        for i in comentarios:
            # print(i.user)
            # print(i.content)
            # print(i.timestamp)
            comentarios_data = {}
            comentarios_data["id_comentario"] = i.id
            comentarios_data['user'] = i.user.username
            comentarios_data['content'] = i.content
            comentarios_data["time"] = i.timestamp
            
            lista.append(comentarios_data)
        lista.append({"count": post.get_comment_count})
        # DjangoJSONEncoder es necesario para poder serializar fechas
        data = json.dumps(lista, cls=DjangoJSONEncoder)
        """
        comentarios = Comment.objects.all()
        data = serialize('json',comentarios)
        """
        # print(type(data))
        return HttpResponse(data, 'application/json')
    def marcar_view(self,object):
        if self.request.user.is_authenticated:
            PostView.objects.create(user=self.request.user, post=object)
        


    def get_object(self, **kwargs):
        #print(self.request.COOKIES)
        object = super().get_object(**kwargs)

        try:
            view = PostView.objects.filter(user=self.request.user, post=object).order_by('-timestamp')[0]
            print(view.timestamp)
        except:
            self.marcar_view(object)

        else:
            # print(type(view.timestamp))
            fecha_view = view.timestamp

            dia_view = fecha_view.date()
            # print(dia_view)
            fecha_actual = datetime.utcnow().date()
            #print(fecha_actual)
            # print(fecha_actual)
            diferencia = fecha_actual-dia_view
            # print(diferencia)
            if diferencia == timedelta(0, 0, 0, 0, 0, 0, 0):
                #print("Mismo dia")
                hora_view = fecha_view.time()
                hora_actual = datetime.utcnow().time()
                # print(hora_actual-hora_view)
                # print((hora_view.hour))
                # print(hora_actual.hour)
                if hora_view.hour == hora_actual.hour:
                    #print("Misma Hora")
                    diferencia_minutos = hora_actual.minute - hora_view.minute

                    if diferencia_minutos > 15:
                        self.marcar_view(object)
                    else:
                        #print("Recien visto")
                        pass
                else:
                    #print("Diferente hora")
                    self.marcar_view(object)
                # print(fecha_view.time())
                # print(datetime.utcnow().time())

            else:
                #print("Diferente dia")
                #print(diferencia)

                self.marcar_view(object)

        return object
        
def setCommentView(request,id):
    #print("Hola")
    #visto = False
    lista = []
    #print(request.user.is_authenticated)
    if request.user.is_authenticated:

        if request.is_ajax():
            print("Es ajax")
            try:
                comment = Comment.objects.filter(id=id)[0]
                commentView = CommentView.objects.filter(comment=comment,user=request.user)[0]
                print("Ya hay una vista")
                visto = True
                
            except:
                comment = Comment.objects.filter(id=id)[0]
                commentView = CommentView.objects.create(comment=comment,user=request.user)

    else:
        visto = True

    print(visto)

    dic = {}
    dic["visto"] = visto
    lista.append(dic)  
    data = json.dumps(lista)     
    return HttpResponse(data,'application/json')



class PostCreateView(CreateView):

    form_class = PostForm
    model = Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        titulo_slug = self.object.title
        new_slug = ""
        for i in range(len(titulo_slug)):
            if titulo_slug[i] in ("?","!","#","$","&","'","(",")","*",",","/",":",";","=","@","[","]","+"):
               new_slug += "signo"
            else:
                new_slug += titulo_slug[i]
        print(new_slug)
        try:

            p = Post.objects.all().order_by('-id').first()
            id_last_post = p.id+1
        except:
            id_last_post = 1
        
            

        self.object.slug = str(id_last_post)+" " + \
            str(new_slug)+" "+str(self.object.author)
        # print(self.object.slug)
        self.object.save()
        return redirect("/")

    def get_initial(self, *args, **kwargs):
        initial = super(PostCreateView, self).get_initial(**kwargs)
        initial['author'] = self.request.user
        initial['slug'] = ""
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create',
            'search_form': SearchForm()
        })
        return context
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            
            return super().get(request, *args, **kwargs)
        return redirect("login")
    # ando viendo como agregar author


class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update',
            'objeto': self.get_object(),
            'search_form': SearchForm()
        })
        #print(context)
        return context

    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        return object


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            
            'search_form': SearchForm()
        })
        #print(context)
        return context








def like(request, slug):

    if request.user.is_authenticated:
        
        if request.is_ajax():
            #print("Hola")
            post = get_object_or_404(Post, slug=slug)
            #print("1")
            like_qs = Like.objects.filter(user=request.user, post=post)
            #print("2")
            if like_qs.exists():
                #print("3")
                #print("Hola")
                like_qs[0].delete()
                likes = post.get_like_count
                post_id = post.id
                # print(likes)

                lista_likes = []
                data_likes = {"likes": likes, "post": post_id}
                lista_likes.append(data_likes)
                data = json.dumps(lista_likes)
                #print("4")

                # print(data)
                return HttpResponse(data, 'application/json')
            #print("5")
            Like.objects.create(user=request.user, post=post)
            likes = post.get_like_count
            post_id = post.id
            #print("6")
            # print(likes)

            lista_likes = []
            data_likes = {"likes": likes, "post": post_id}
            lista_likes.append(data_likes)
            data = json.dumps(lista_likes)
            #print("7")
            #print(data)
            return HttpResponse(data, 'application/json')
        
    else:
        #print("Hola")
        data = json.dumps([{"activo":"False"}])
        #print(data)
        return HttpResponse(data, 'application/json')


