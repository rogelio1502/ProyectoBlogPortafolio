
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from Blog.settings.production import DEBUG
from Blog.settings.base import STATIC_ROOT,STATIC_URL,MEDIA_ROOT,MEDIA_URL
from django.conf.urls.static import static
from django.contrib.auth.views import auth_login,auth_logout




from posts.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView,
    like,
    setCommentView,
    

    
)
from usuario.views import (
    UserListView,
    UserDetailView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    #codigo obtenido de django all auth documentation   
    path('accounts/', include('usuario.urls')),

    path('accounts/', include('django.contrib.auth.urls')), # new


    
    path('users/',UserListView.as_view(),name="users"),
    
    path('',PostListView.as_view(),name="list"),

    path('create/',PostCreateView.as_view(),name="create"),

    path('<slug>/',PostDetailView.as_view(),name="detail"),
    path('users/<slug>/',UserDetailView.as_view(),name="user"),
    path('<slug>/update/',PostUpdateView.as_view(),name="update"),
    path('<slug>/delete/',PostDeleteView.as_view(),name="delete"),
    path('comentarios/<id>/',setCommentView,name="setView"),

    path('like/<slug>/',like,name="like"),
]
urlpatterns+=static(STATIC_URL, document_root=STATIC_ROOT)


#if DEBUG == True:
#    urlpatterns+=static(MEDIA_URL, document_root=MEDIA_ROOT)
