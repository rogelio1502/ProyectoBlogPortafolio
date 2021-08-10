
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import auth_login,auth_logout




from posts.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView,
    like,
    UserListView,
    
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
    path('<slug>/update/',PostUpdateView.as_view(),name="update"),
    path('<slug>/delete/',PostDeleteView.as_view(),name="delete"),
    path('like/<slug>/',like,name="like"),
]


if settings.DEBUG == False:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

