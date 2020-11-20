from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("entrar/", views.Login.as_view(), name="login"),
    path("sair/", views.Logout.as_view(), name="logout"),
    path("cadastre-se/", views.register, name="register"),
    path("nova-senha/", views.password_reset, name="password_reset"),
    path("confirmar-nova-senha/<str:key>/", views.password_reset_confirm, name="password_reset_confirm"),
    path("editar/",  views.edit, name="edit"),
    path("editar-senha/", views.edit_password, name="edit_password"),
]