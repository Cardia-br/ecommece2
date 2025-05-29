from django.urls import path
from .views import (
    ProdutoListView, ProdutoCreateView,
    ProdutoUpdateView, ProdutoDeleteView,
    LoginView, LogoutView, RegisterView
)

urlpatterns = [
    path('', ProdutoListView.as_view(), name='listar_produtos'),
    path('adicionar/', ProdutoCreateView.as_view(), name='adicionar_produto'),
    path('editar/<int:pk>/', ProdutoUpdateView.as_view(), name='editar_produto'),
    path('remover/<int:pk>/', ProdutoDeleteView.as_view(), name='remover_produto'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]