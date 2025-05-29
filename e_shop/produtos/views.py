from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Produto
from .forms import ProdutoForm
from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.mixins import LoginRequiredMixin

class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'produtos/lista.html'
    context_object_name = 'produtos'

class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtos/form.html'
    success_url = reverse_lazy('listar_produtos')

class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtos/form.html'
    success_url = reverse_lazy('listar_produtos')

class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'produtos/confirm_delete.html'
    success_url = reverse_lazy('listar_produtos')


# Tela de login
class LoginView(AuthLoginView):
    template_name = 'login.html'

# Tela de logout
class LogoutView(AuthLogoutView):
    next_page = reverse_lazy('login')

# Tela de cadastro
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')