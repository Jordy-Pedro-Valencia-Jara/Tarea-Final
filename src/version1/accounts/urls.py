from django.urls import path
from . import views

urlpatterns=[
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("createimg",views.createimg,name="createimg"),
    path("listar",views.listar,name="listar"),
    path("eliminar/<id>/",views.eliminar,name="eliminar"),
    path("modificar/<id>/",views.modificar,name="modificar")
]