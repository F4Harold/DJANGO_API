from django.urls import path, unclude 

from rest_framework.routers import DefaultRouter

from .Views import (
    auditoria_loginViewSet,
    credencialViewSet,
    rolViewSet,
    tipo_documentoViewSet,
    usuarioViewSet,
    usuario_rolViewSet
)
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()

router.register(r'auditoria_login', auditoria_loginViewSet)
router.register(r'credencial', credencialViewSet)
router.register(r'rol', rolViewSet)
router.register(r'tipo_documento', tipo_documentoViewSet)
router.register(r'usuario', usuarioViewSet)
router.register(r'usuario_rol', usuario_rolViewSet)

urlspatterns = [
    path('', incluede(router.urls))
]
