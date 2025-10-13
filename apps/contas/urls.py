from django.urls import include, path 
from contas import views

urlpatterns = [
    path('desconectado-inatividade/',  views.timeout_view, name='timeout'), 
    path('entrar/', views.login_view, name='login'), #login
    path('criar-conta/', views.register_view, name='register'), #registrar
    path('sair/', views.logout_view, name='logout'), #logout
    path('atualizar-usuario/<int:user_id>/', views.atualizar_usuario, name='atualizar_usuario'), #atualizar user
    path("", include("django.contrib.auth.urls"))
]