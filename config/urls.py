"""
URL configuration for config project.

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
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from gestao.views import (
    alunoViewSet, cursoViewSet, matriculaViewSet,
    disciplinaViewSet, professorViewSet, turmaViewSet, frequenciaViewSet
)
router = DefaultRouter()
router.register(r'alunos', alunoViewSet)
router.register(r'cursos', cursoViewSet)
router.register(r'matriculas', matriculaViewSet)
router.register(r'disciplinas', disciplinaViewSet)
router.register(r'professores', professorViewSet)
router.register(r'turmas', turmaViewSet,)
router.register(r'frequencias', frequenciaViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

