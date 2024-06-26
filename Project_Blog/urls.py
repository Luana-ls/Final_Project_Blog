"""
URL configuration for Project_Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from cadastro.views import cadastroModelViewSet
from django.conf import settings
from django.conf.urls.static import static
from cadastro.views import cadastrar, login, usuario
from inicio.views import inicio, sobre, contato
from post.views import Post

router = SimpleRouter(trailing_slash=False)
router.register('cadastro', cadastroModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio), #ok
    path('cadastro/', cadastrar), # ???
    path('login/', login), #OK
    path('usuario/', usuario),  #OK   
    path('sobre/', sobre), #OK
    path('contato/', contato), #OK
    path('post/', Post), #OK
]
urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
