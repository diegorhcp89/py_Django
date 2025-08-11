from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import home, about, contact, SimpleClassView, user_profile, home_template, listar_produtos, exibir_dados, listar_produto, contatoform, registro, login_usuario

urlpatterns = [
    path("", home, name="home"),
    path('sobre/', about, name="about"),
    path('contato/', contact, name="contact"),
    path('cbv/', SimpleClassView.as_view(), name="cbv"),
    path('user/<int:id>', user_profile, name="user_profile"),
    path('home/', home_template, name="home_template"),
    path('produtos/', listar_produtos, name="listar_produtos"),
    path('filtros/', exibir_dados, name="exibir_dados"),
    path('produto/', listar_produto, name='listar_produto'),
    path('contatoform/',contatoform, name="contato_form"),
    path('registro/',registro, name="registro"),
    path('login/',login_usuario, name="login"),
    path('logout', LogoutView.as_view(), name="logout")
]
