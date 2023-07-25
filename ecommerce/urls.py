"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import statistics
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from produtos.views import index, detalhe_produto,administrativo, produto_criar, produto_editar, produto_remover

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('produto/<int:id>/', detalhe_produto, name='detalhe_produto'),
    path('administrativo/', administrativo, name='administrativo'),
    path('administrativo/criar/', produto_criar, name='produto_criar'),
    path('administrativo/editar/<int:id>/', produto_editar, name='produto_editar'),
    path('administrativo/remover/<int:id>', produto_remover, name='produto_remover')
    
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
