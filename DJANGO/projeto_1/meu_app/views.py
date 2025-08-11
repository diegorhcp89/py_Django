from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Produto
from .forms import ContatoForm
from .forms import RegistroUsuarioForm

# Create your views here.
def home(request):
    return HttpResponse("Bem-vindo ao meu primeiro app Django!")

def about(request):
    return HttpResponse("Sobre nós - Infomações da empresa")

def contact(request):
    return HttpResponse("Entre em contato")

class SimpleClassView(View):
    def get(self, request):
        return HttpResponse("Está é uma view de classe CBV")

def user_profile(request, id):
    # chamada do banco de dados pegando o usuário por id
    # organizaria os campos para enviar o template
    # renderizaria um template com os dados do usuario
    return HttpResponse(f"Perfil do usuário com ID: {id}")

def home_template(request):
    return render(request, 'home.html')

def listar_produtos(request):
    produtos = Produto.objects.all()

    return render(request, 'produtos.html', {'produtos': produtos})

def exibir_dados(request):
    contexto = {
        "nome": "Django",
        "numero": 42,
        "lista": ["Python", "Django", "Flask"],
        "descricao": ""
    }

    return render(request, "exemplo_filtros.html", contexto)

def listar_produto(request):
    produtos = [
        {"nome": "Celular", "preco": 1500},
        {"nome": "Notebook", "preco": 2500},
        {"nome": "Fone de ouvido", "preco": 500}
    ]

    return render(request, "lista_produtos.html", {"produtos": produtos})

def contatoform(request):

    if request.method == "POST":
        form = ContatoForm(request.POST)

        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            msg = form.cleaned_data['mensagem']

            print(f"Enviado e-mail de {nome} {email}, com a mensagem: {msg}")

            messages.success(request, "Mendagem enviada com sucesso!")

            return HttpResponseRedirect("/contatoform/")
        else:
            messages.error(request, "Erro no formulario. Verifique os campos!")

    else:
        form = ContatoForm()
    return render(request, "contato.html", {"form": form})

def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home_template")

    else:
        form = RegistroUsuarioForm()

    return render(request, "registro.html", {"form": form})

def login_usuario(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home_template")

    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})
