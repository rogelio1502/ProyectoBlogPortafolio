from django.urls import path

from .views import SignUpView,LoginView,PasswordChangeView,PasswordChangeDoneView


urlpatterns = [
    path('password_change/done/',PasswordChangeDoneView.as_view(),name="password_change_done"),
    path('password_change/',PasswordChangeView.as_view(),name="password_change"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/',LoginView.as_view(),name='login'),
]