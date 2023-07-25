from django.shortcuts import get_object_or_404, redirect, render
from produtos.forms import ProdutoForm
from .models import Produto

def index(request):
    produto = Produto.objects.all()
    context = {
        'produto' : produto,
    }
    return render(request, "vendas/index.html", context)

def detalhe_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produtos_similares = Produto.objects.filter(marca=produto.marca).exclude(id=id)[:3]
    context = {
        'produto':produto,
        'produtos_similares': produtos_similares
    }
    return render(request, 'vendas/detalhe_produto.html',context )

def administrativo(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'vendas/administrativo.html', context)

def produto_criar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProdutoForm()
            
    else:
        form = ProdutoForm()
    return render(request, 'vendas/forms.html',{'form':form,})

def produto_editar(request,id):
    produto = get_object_or_404(Produto,id=id)
   
    if request.method == 'POST':
        form = ProdutoForm(request.POST,instance=produto)

        if form.is_valid():
            form.save()
            return redirect('administrativo')
    else:
        form = ProdutoForm(instance=produto)

    return render(request,'vendas/forms.html',{'form':form})

def produto_remover(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('administrativo')
# Create your views here.
