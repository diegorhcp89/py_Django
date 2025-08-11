from django import forms
from .models import Cliente

class ContatoForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label="E-mail")
    mensagem = forms.CharField(widget=forms.Textarea, label="Mensagem")
