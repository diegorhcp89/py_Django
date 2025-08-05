from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

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
